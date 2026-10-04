// AZIA Figma Plugin Sandbox Execution Layer (High-Fidelity Render Engine)
figma.showUI(__html__, { width: 440, height: 680, themeColors: true });

figma.ui.onmessage = async (msg) => {
  switch (msg.type) {
    case "AZIA_INSPECT_SELECTION":
      inspectSelection();
      break;
    case "AZIA_EXECUTE_OPERATIONS":
      await executeOperations(msg.payload);
      break;
    case "AZIA_ROLLBACK_GENERATION":
      rollbackGeneration(msg.payload?.generation_id);
      break;
    case "AZIA_CREATE_ANNOTATION":
      await createAnnotationOnSelection(msg.payload);
      break;
    default:
      console.warn("Unknown message:", msg.type);
  }
};

function inspectSelection() {
  const selection = figma.currentPage.selection;
  if (!selection || selection.length === 0) {
    figma.ui.postMessage({
      type: "SELECTION_INSPECTED",
      payload: { has_selection: false, message: "No layer selected. Select a frame to audit." }
    });
    return;
  }
  const node = selection[0];
  figma.ui.postMessage({
    type: "SELECTION_INSPECTED",
    payload: {
      has_selection: true,
      id: node.id,
      name: node.name,
      type: node.type,
      width: node.width,
      height: node.height,
      is_managed_by_azia: node.getPluginData("managed_by") === "autonomous-design-mcp",
      generation_id: node.getPluginData("generation_id")
    }
  });
}

function hexToRgb(hex) {
  if (!hex) return { r: 0.95, g: 0.96, b: 0.98 };
  hex = hex.replace("#", "");
  if (hex.length === 3) hex = hex.split("").map(c => c + c).join("");
  const num = parseInt(hex, 16);
  if (isNaN(num)) return { r: 0.95, g: 0.96, b: 0.98 };
  return { r: ((num >> 16) & 255) / 255, g: ((num >> 8) & 255) / 255, b: (num & 255) / 255 };
}

function setPositionInParent(node, op, parent) {
  let x = op.payload?.x || 0;
  let y = op.payload?.y || 0;
  if (parent && parent.type === "SECTION") {
    // In Figma, child coordinates of SectionNode are relative to section origin
    if (x >= parent.x) x = x - parent.x;
    if (y >= parent.y) y = y - parent.y;
  }
  node.x = x;
  node.y = y;
}

function renderInstanceNode(op, parent, createdNodes, generation_id) {
  const masterId = op.payload?.master_component_id || op.payload?.component_id;
  const content = op.payload?.content_data || {};

  const node = figma.createFrame();
  node.name = op.name || "Instance";
  node.setPluginData("managed_by", "autonomous-design-mcp");
  node.setPluginData("generation_id", generation_id);
  if (masterId) node.setPluginData("master_component_id", masterId);

  node.layoutAlign = "STRETCH";
  node.primaryAxisSizingMode = "AUTO";
  node.counterAxisSizingMode = "AUTO";

  if (masterId === "cmp_btn_primary") {
    // Primary Action Button
    node.layoutMode = "HORIZONTAL";
    node.primaryAxisAlignItems = "CENTER";
    node.counterAxisAlignItems = "CENTER";
    node.itemSpacing = 8;
    node.paddingTop = 14;
    node.paddingBottom = 14;
    node.paddingLeft = 20;
    node.paddingRight = 20;
    node.cornerRadius = 10;
    node.fills = [{ type: "SOLID", color: hexToRgb("#EA580C") }];

    const labelText = figma.createText();
    labelText.characters = content.label || op.name;
    labelText.fontSize = 14;
    try { labelText.fontName = { family: "Inter", style: "Bold" }; } catch (e) {}
    labelText.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
    node.appendChild(labelText);

    if (content.badge) {
      const badgePill = figma.createFrame();
      badgePill.layoutMode = "HORIZONTAL";
      badgePill.paddingLeft = 8;
      badgePill.paddingRight = 8;
      badgePill.paddingTop = 2;
      badgePill.paddingBottom = 2;
      badgePill.cornerRadius = 9999;
      badgePill.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
      const badgeText = figma.createText();
      badgeText.characters = String(content.badge);
      badgeText.fontSize = 11;
      try { badgeText.fontName = { family: "Inter", style: "Bold" }; } catch (e) {}
      badgeText.fills = [{ type: "SOLID", color: hexToRgb("#EA580C") }];
      badgePill.appendChild(badgeText);
      node.appendChild(badgePill);
    }
  } else if (masterId === "cmp_btn_secondary") {
    // Secondary Action Button / Pill
    node.layoutMode = "HORIZONTAL";
    node.primaryAxisAlignItems = "CENTER";
    node.counterAxisAlignItems = "CENTER";
    node.paddingTop = 10;
    node.paddingBottom = 10;
    node.paddingLeft = 14;
    node.paddingRight = 14;
    node.cornerRadius = 8;
    node.fills = [{ type: "SOLID", color: hexToRgb("#F1F5F9") }];
    node.strokes = [{ type: "SOLID", color: hexToRgb("#CBD5E1") }];

    const labelText = figma.createText();
    labelText.characters = content.label || op.name;
    labelText.fontSize = 13;
    try { labelText.fontName = { family: "Inter", style: "Medium" }; } catch (e) {}
    labelText.fills = [{ type: "SOLID", color: hexToRgb("#1E293B") }];
    node.appendChild(labelText);
  } else if (masterId === "cmp_search_bar") {
    // Search Bar
    node.layoutMode = "HORIZONTAL";
    node.counterAxisAlignItems = "CENTER";
    node.paddingTop = 10;
    node.paddingBottom = 10;
    node.paddingLeft = 14;
    node.paddingRight = 14;
    node.cornerRadius = 10;
    node.fills = [{ type: "SOLID", color: hexToRgb("#F8FAFC") }];
    node.strokes = [{ type: "SOLID", color: hexToRgb("#E2E8F0") }];

    const searchIcon = figma.createText();
    searchIcon.characters = "🔍  " + (content.placeholder || "Search dishes, restaurants, groceries...");
    searchIcon.fontSize = 13;
    try { searchIcon.fontName = { family: "Inter", style: "Regular" }; } catch (e) {}
    searchIcon.fills = [{ type: "SOLID", color: hexToRgb("#94A3B8") }];
    node.appendChild(searchIcon);
  } else if (masterId === "cmp_status_badge") {
    // Status Badge / Filter Pill
    node.layoutMode = "HORIZONTAL";
    node.counterAxisAlignItems = "CENTER";
    node.paddingTop = 6;
    node.paddingBottom = 6;
    node.paddingLeft = 14;
    node.paddingRight = 14;
    node.cornerRadius = 9999;
    node.layoutAlign = "INHERIT";

    const isActive = content.active === true || content.color === "success";
    if (isActive) {
      node.fills = [{ type: "SOLID", color: hexToRgb("#EA580C") }];
    } else {
      node.fills = [{ type: "SOLID", color: hexToRgb("#F1F5F9") }];
      node.strokes = [{ type: "SOLID", color: hexToRgb("#E2E8F0") }];
    }

    const badgeText = figma.createText();
    badgeText.characters = content.label || op.name;
    badgeText.fontSize = 12;
    try { badgeText.fontName = { family: "Inter", style: isActive ? "Bold" : "Medium" }; } catch (e) {}
    badgeText.fills = [{ type: "SOLID", color: isActive ? { r: 1, g: 1, b: 1 } : hexToRgb("#475569") }];
    node.appendChild(badgeText);
  } else if (masterId === "cmp_input_field") {
    // Input Field
    node.layoutMode = "VERTICAL";
    node.itemSpacing = 6;
    node.fills = [];

    if (content.label) {
      const lbl = figma.createText();
      lbl.characters = content.label;
      lbl.fontSize = 12;
      try { lbl.fontName = { family: "Inter", style: "Semi Bold" }; } catch (e) {}
      lbl.fills = [{ type: "SOLID", color: hexToRgb("#475569") }];
      node.appendChild(lbl);
    }

    const inputBox = figma.createFrame();
    inputBox.layoutMode = "HORIZONTAL";
    inputBox.layoutAlign = "STRETCH";
    inputBox.paddingTop = 10;
    inputBox.paddingBottom = 10;
    inputBox.paddingLeft = 12;
    inputBox.paddingRight = 12;
    inputBox.cornerRadius = 8;
    inputBox.fills = [{ type: "SOLID", color: hexToRgb("#F8FAFC") }];
    inputBox.strokes = [{ type: "SOLID", color: hexToRgb("#CBD5E1") }];

    const valText = figma.createText();
    valText.characters = content.value || content.placeholder || "Enter text...";
    valText.fontSize = 13;
    try { valText.fontName = { family: "Inter", style: "Regular" }; } catch (e) {}
    valText.fills = [{ type: "SOLID", color: hexToRgb("#0F172A") }];
    inputBox.appendChild(valText);
    node.appendChild(inputBox);
  } else if (masterId === "cmp_entity_card") {
    // Entity Content Card
    node.layoutMode = "VERTICAL";
    node.paddingTop = 14;
    node.paddingBottom = 14;
    node.paddingLeft = 16;
    node.paddingRight = 16;
    node.itemSpacing = 8;
    node.cornerRadius = 12;
    node.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
    node.strokes = [{ type: "SOLID", color: hexToRgb("#E2E8F0") }];

    // Header row
    const title = content.name || content.title || content.key;
    if (title) {
      const headerRow = figma.createFrame();
      headerRow.layoutMode = "HORIZONTAL";
      headerRow.layoutAlign = "STRETCH";
      headerRow.primaryAxisAlignItems = "SPACE_BETWEEN";
      headerRow.counterAxisAlignItems = "CENTER";
      headerRow.fills = [];

      const titleText = figma.createText();
      titleText.characters = title;
      titleText.fontSize = 14;
      try { titleText.fontName = { family: "Inter", style: "Bold" }; } catch (e) {}
      titleText.fills = [{ type: "SOLID", color: hexToRgb("#0F172A") }];
      headerRow.appendChild(titleText);

      if (content.badge) {
        const badgeFrame = figma.createFrame();
        badgeFrame.layoutMode = "HORIZONTAL";
        badgeFrame.paddingTop = 2;
        badgeFrame.paddingBottom = 2;
        badgeFrame.paddingLeft = 6;
        badgeFrame.paddingRight = 6;
        badgeFrame.cornerRadius = 4;
        badgeFrame.fills = [{ type: "SOLID", color: hexToRgb("#FEF3C7") }];
        const badgeTxt = figma.createText();
        badgeTxt.characters = content.badge;
        badgeTxt.fontSize = 10;
        try { badgeTxt.fontName = { family: "Inter", style: "Bold" }; } catch (e) {}
        badgeTxt.fills = [{ type: "SOLID", color: hexToRgb("#B45309") }];
        badgeFrame.appendChild(badgeTxt);
        headerRow.appendChild(badgeFrame);
      }
      node.appendChild(headerRow);
    }

    // Description / Cuisine / Customization
    const desc = content.desc || content.customization || content.cuisine || content.dorm_landmark;
    if (desc) {
      const descText = figma.createText();
      descText.characters = desc;
      descText.fontSize = 12;
      try { descText.fontName = { family: "Inter", style: "Regular" }; } catch (e) {}
      descText.fills = [{ type: "SOLID", color: hexToRgb("#64748B") }];
      node.appendChild(descText);
    }

    // Meta row (Rating, ETA, Price, etc.)
    const metaParts = [];
    if (content.rating) metaParts.push("⭐ " + content.rating);
    if (content.delivery_time) metaParts.push("⏱ " + content.delivery_time);
    if (content.delivery_fee) metaParts.push("🛵 " + content.delivery_fee);
    if (content.price) metaParts.push(content.price);
    if (content.points) metaParts.push("🎯 " + content.points);
    if (content.cycle_time) metaParts.push("⚡ " + content.cycle_time);

    if (metaParts.length > 0) {
      const metaText = figma.createText();
      metaText.characters = metaParts.join(" • ");
      metaText.fontSize = 12;
      try { metaText.fontName = { family: "Inter", style: "Medium" }; } catch (e) {}
      metaText.fills = [{ type: "SOLID", color: hexToRgb("#EA580C") }];
      node.appendChild(metaText);
    }

    // Key-Value rows for Bill Summaries
    const kvKeys = Object.keys(content).filter(k => 
      !["id", "name", "title", "desc", "customization", "cuisine", "dorm_landmark", "rating", "delivery_time", "delivery_fee", "price", "badge", "points", "cycle_time", "key"].includes(k)
    );
    for (const k of kvKeys) {
      if (typeof content[k] === "string" || typeof content[k] === "number") {
        const kvRow = figma.createFrame();
        kvRow.layoutMode = "HORIZONTAL";
        kvRow.layoutAlign = "STRETCH";
        kvRow.primaryAxisAlignItems = "SPACE_BETWEEN";
        kvRow.fills = [];

        const kText = figma.createText();
        kText.characters = k;
        kText.fontSize = 12;
        try { kText.fontName = { family: "Inter", style: "Regular" }; } catch (e) {}
        kText.fills = [{ type: "SOLID", color: hexToRgb("#64748B") }];
        kvRow.appendChild(kText);

        const vText = figma.createText();
        vText.characters = String(content[k]);
        vText.fontSize = 12;
        try { vText.fontName = { family: "Inter", style: k.toLowerCase().includes("total") ? "Bold" : "Medium" }; } catch (e) {}
        vText.fills = [{ type: "SOLID", color: k.toLowerCase().includes("total") ? hexToRgb("#EA580C") : hexToRgb("#0F172A") }];
        kvRow.appendChild(vText);

        node.appendChild(kvRow);
      }
    }
  } else if (masterId === "cmp_global_nav") {
    // Bottom Navigation Bar
    node.layoutMode = "HORIZONTAL";
    node.primaryAxisAlignItems = "SPACE_BETWEEN";
    node.counterAxisAlignItems = "CENTER";
    node.paddingTop = 12;
    node.paddingBottom = 12;
    node.paddingLeft = 24;
    node.paddingRight = 24;
    node.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
    node.strokes = [{ type: "SOLID", color: hexToRgb("#E2E8F0") }];

    const navItems = [
      { icon: "🏠", label: "Home", active: true },
      { icon: "🔍", label: "Search", active: false },
      { icon: "🛍️", label: "Cart", active: false },
      { icon: "👤", label: "Account", active: false }
    ];
    for (const item of navItems) {
      const itemFrame = figma.createFrame();
      itemFrame.layoutMode = "VERTICAL";
      itemFrame.primaryAxisAlignItems = "CENTER";
      itemFrame.counterAxisAlignItems = "CENTER";
      itemFrame.itemSpacing = 2;
      itemFrame.fills = [];

      const iconText = figma.createText();
      iconText.characters = item.icon;
      iconText.fontSize = 16;
      itemFrame.appendChild(iconText);

      const labelText = figma.createText();
      labelText.characters = item.label;
      labelText.fontSize = 10;
      try { labelText.fontName = { family: "Inter", style: item.active ? "Bold" : "Medium" }; } catch (e) {}
      labelText.fills = [{ type: "SOLID", color: item.active ? hexToRgb("#EA580C") : hexToRgb("#94A3B8") }];
      itemFrame.appendChild(labelText);

      node.appendChild(itemFrame);
    }
  } else {
    // Default fallback instance
    node.layoutMode = "HORIZONTAL";
    node.counterAxisAlignItems = "CENTER";
    node.paddingTop = 10;
    node.paddingBottom = 10;
    node.paddingLeft = 14;
    node.paddingRight = 14;
    node.cornerRadius = 8;
    node.fills = [{ type: "SOLID", color: hexToRgb("#F8FAFC") }];
    node.strokes = [{ type: "SOLID", color: hexToRgb("#E2E8F0") }];

    const t = figma.createText();
    t.characters = content.label || content.name || content.title || op.name;
    t.fontSize = 13;
    try { t.fontName = { family: "Inter", style: "Medium" }; } catch (e) {}
    t.fills = [{ type: "SOLID", color: hexToRgb("#0F172A") }];
    node.appendChild(t);
  }

  if (parent && "appendChild" in parent) {
    parent.appendChild(node);
  }
  return node;
}

async function executeOperations(payload) {
  let operations = [];
  let generation_id = "gen_azia";
  let product_name = "AZIA Design";

  if (Array.isArray(payload)) {
    operations = payload;
  } else if (payload && Array.isArray(payload.operations)) {
    operations = payload.operations;
    generation_id = payload.generation_id || payload.metadata?.generation_id || generation_id;
    product_name = payload.product_name || payload.metadata?.product_name || product_name;
  } else if (payload && payload.figma_payload && Array.isArray(payload.figma_payload.operations)) {
    operations = payload.figma_payload.operations;
    generation_id = payload.figma_payload.metadata?.generation_id || generation_id;
    product_name = payload.figma_payload.metadata?.product_name || product_name;
  } else if (payload && payload.payload && Array.isArray(payload.payload.operations)) {
    operations = payload.payload.operations;
    generation_id = payload.payload.generation_id || payload.payload.metadata?.generation_id || generation_id;
    product_name = payload.payload.product_name || payload.payload.metadata?.product_name || product_name;
  }

  figma.notify("AZIA: Rendering " + product_name + " (" + operations.length + " ops)...");
  try {
    await figma.loadFontAsync({ family: "Inter", style: "Regular" });
    await figma.loadFontAsync({ family: "Inter", style: "Medium" });
    await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
    await figma.loadFontAsync({ family: "Inter", style: "Bold" });
  } catch (err) {
    console.warn("Font pre-load warning:", err);
  }

  const createdNodes = {};
  let renderedCount = 0;

  for (const op of operations) {
    try {
      const parent = op.parent_id ? createdNodes[op.parent_id] : figma.currentPage;

      if (op.op_type === "create_page") {
        if (figma.currentPage.name === "Page 1") {
          figma.currentPage.name = op.name;
        }
        createdNodes[op.target_id] = figma.currentPage;
        renderedCount++;
      } else if (op.op_type === "create_section" && "createSection" in figma) {
        const sec = figma.createSection();
        sec.name = op.name;
        sec.x = op.payload?.x || 0;
        sec.y = op.payload?.y || 0;
        sec.resizeWithoutConstraints(op.payload?.width || 1200, op.payload?.height || 800);
        sec.setPluginData("managed_by", "autonomous-design-mcp");
        sec.setPluginData("generation_id", generation_id);
        createdNodes[op.target_id] = sec;
        renderedCount++;
      } else if (op.op_type === "create_screen" || op.op_type === "create_frame") {
        const frame = figma.createFrame();
        frame.name = op.name;
        setPositionInParent(frame, op, parent);
        frame.resize(op.payload?.width || 393, op.payload?.height || 852);

        // Responsive Auto-Layout Container
        frame.layoutMode = op.payload?.direction === "horizontal" ? "HORIZONTAL" : "VERTICAL";
        frame.paddingTop = op.payload?.padding_top || 0;
        frame.paddingBottom = op.payload?.padding_bottom || 0;
        frame.paddingLeft = op.payload?.padding_x || 0;
        frame.paddingRight = op.payload?.padding_x || 0;
        frame.itemSpacing = op.payload?.gap || 12;
        frame.clipsContent = true;

        if (op.payload?.bg_hex) {
          frame.fills = [{ type: "SOLID", color: hexToRgb(op.payload.bg_hex) }];
        }

        frame.setPluginData("managed_by", "autonomous-design-mcp");
        frame.setPluginData("generation_id", generation_id);
        frame.setPluginData("screen_id", op.target_id);

        if (parent && "appendChild" in parent) parent.appendChild(frame);
        createdNodes[op.target_id] = frame;
        renderedCount++;
      } else if (op.op_type === "create_component") {
        const comp = figma.createComponent();
        comp.name = op.name;
        comp.layoutMode = op.payload?.direction === "vertical" ? "VERTICAL" : "HORIZONTAL";
        comp.paddingTop = op.payload?.padding_y || 10;
        comp.paddingBottom = op.payload?.padding_y || 10;
        comp.paddingLeft = op.payload?.padding_x || 16;
        comp.paddingRight = op.payload?.padding_x || 16;
        comp.itemSpacing = op.payload?.gap || 8;
        comp.cornerRadius = op.payload?.radius || 8;
        comp.resize(op.payload?.width || 320, op.payload?.height || 48);

        let bgRgb = { r: 0.95, g: 0.96, b: 0.98 };
        let textRgb = { r: 0.06, g: 0.09, b: 0.16 };
        if (op.payload?.bg_token === "primary") {
          bgRgb = hexToRgb("#EA580C");
          textRgb = { r: 1, g: 1, b: 1 };
        } else if (op.payload?.bg_token === "secondary") {
          bgRgb = hexToRgb("#3B82F6");
          textRgb = { r: 1, g: 1, b: 1 };
        } else if (op.payload?.bg_token === "surface") {
          bgRgb = { r: 1, g: 1, b: 1 };
          comp.strokes = [{ type: "SOLID", color: hexToRgb("#E2E8F0") }];
        } else if (op.payload?.bg_token === "accent") {
          bgRgb = hexToRgb("#10B981");
          textRgb = { r: 1, g: 1, b: 1 };
        }
        comp.fills = [{ type: "SOLID", color: bgRgb }];

        const compText = figma.createText();
        compText.characters = op.name;
        compText.fontSize = 13;
        try { compText.fontName = { family: "Inter", style: "Medium" }; } catch (e) {}
        compText.fills = [{ type: "SOLID", color: textRgb }];
        comp.appendChild(compText);

        comp.setPluginData("managed_by", "autonomous-design-mcp");
        comp.setPluginData("generation_id", generation_id);

        if (parent && "appendChild" in parent) {
          comp.x = 80;
          comp.y = op.payload?.y || (renderedCount * 60);
          parent.appendChild(comp);
        }
        createdNodes[op.target_id] = comp;
        renderedCount++;
      } else if (op.op_type === "create_instance") {
        const instNode = renderInstanceNode(op, parent, createdNodes, generation_id);
        createdNodes[op.target_id] = instNode;
        renderedCount++;
      } else if (op.op_type === "create_card" || op.op_type === "create_auto_layout") {
        const frame = figma.createFrame();
        frame.name = op.name;
        frame.layoutMode = op.payload?.direction === "horizontal" ? "HORIZONTAL" : "VERTICAL";
        frame.paddingTop = op.payload?.padding_y ?? (op.payload?.padding ?? 12);
        frame.paddingBottom = op.payload?.padding_y ?? (op.payload?.padding ?? 12);
        frame.paddingLeft = op.payload?.padding_x ?? (op.payload?.padding ?? 16);
        frame.paddingRight = op.payload?.padding_x ?? (op.payload?.padding ?? 16);
        frame.itemSpacing = op.payload?.gap || 8;
        frame.cornerRadius = op.payload?.corner_radius || op.payload?.radius || 0;

        if (op.payload?.bg_color_hex || op.payload?.bg_hex) {
          frame.fills = [{ type: "SOLID", color: hexToRgb(op.payload.bg_color_hex || op.payload.bg_hex) }];
        } else {
          frame.fills = [];
        }

        // Auto-layout sizing
        frame.layoutAlign = "STRETCH";
        frame.primaryAxisSizingMode = "AUTO";
        frame.counterAxisSizingMode = "AUTO";

        frame.setPluginData("managed_by", "autonomous-design-mcp");
        frame.setPluginData("generation_id", generation_id);

        if (parent && "appendChild" in parent) parent.appendChild(frame);
        createdNodes[op.target_id] = frame;
        renderedCount++;
      } else if (op.op_type === "create_text") {
        const textNode = figma.createText();
        textNode.characters = op.payload?.content || op.name;
        textNode.fontSize = op.payload?.font_size || 14;
        if (op.payload?.color_hex) {
          textNode.fills = [{ type: "SOLID", color: hexToRgb(op.payload.color_hex) }];
        }
        textNode.setPluginData("managed_by", "autonomous-design-mcp");
        if (parent && "appendChild" in parent) parent.appendChild(textNode);
        createdNodes[op.target_id] = textNode;
        renderedCount++;
      } else if (op.op_type === "create_sticky_note") {
        if (figma.editorType === "figjam" && "createSticky" in figma) {
          const sticky = figma.createSticky();
          sticky.text.characters = op.payload?.content || op.name;
          setPositionInParent(sticky, op, parent);
          sticky.setPluginData("managed_by", "autonomous-design-mcp");
          sticky.setPluginData("generation_id", generation_id);
          createdNodes[op.target_id] = sticky;
          renderedCount++;
        } else {
          const note = figma.createFrame();
          note.name = op.name;
          setPositionInParent(note, op, parent);
          note.resize(260, 140);
          note.layoutMode = "VERTICAL";
          note.paddingTop = 12;
          note.paddingBottom = 12;
          note.paddingLeft = 12;
          note.paddingRight = 12;
          note.cornerRadius = 6;
          note.fills = [{ type: "SOLID", color: { r: 1, g: 0.96, b: 0.77 } }];
          const noteText = figma.createText();
          noteText.characters = op.payload?.content || op.name;
          noteText.fontSize = 11;
          note.appendChild(noteText);
          if (parent && "appendChild" in parent) parent.appendChild(note);
          createdNodes[op.target_id] = note;
          renderedCount++;
        }
      } else if (op.op_type === "connect_prototype") {
        const sourceNode = createdNodes[op.payload?.source_element_id || op.payload?.source_screen_id];
        const targetNode = createdNodes[op.payload?.target_screen_id];
        if (sourceNode && targetNode && "reactions" in sourceNode) {
          try {
            sourceNode.reactions = [{
              action: {
                type: "NODE",
                destinationId: targetNode.id,
                navigation: "NAVIGATE",
                transition: { type: "DISSOLVE", duration: 0.25 }
              },
              trigger: { type: "ON_CLICK" }
            }];
            renderedCount++;
          } catch (reactErr) {
            // reactions require prototyping access, safe fallback
          }
        }
      }
    } catch (e) {
      console.warn("Operation failed:", op.op_id, e);
    }
  }

  // Focus view directly on the generated screens so they are crisp and immediately visible!
  const screenNodes = Object.values(createdNodes).filter(n => n.getPluginData && n.getPluginData("screen_id"));
  if (screenNodes.length > 0) {
    figma.viewport.scrollAndZoomIntoView(screenNodes.slice(0, 2));
  } else {
    const allCreated = Object.values(createdNodes).filter(n => n.type !== "PAGE");
    if (allCreated.length > 0) {
      figma.viewport.scrollAndZoomIntoView(allCreated);
    }
  }

  figma.notify("AZIA: Successfully rendered " + renderedCount + " high-fidelity nodes! ✨");
  figma.ui.postMessage({ type: "OPERATIONS_COMPLETED", payload: { rendered_count: renderedCount, generation_id } });
}

function rollbackGeneration(generationId) {
  if (!generationId) return;
  let count = 0;
  const nodes = figma.currentPage.findAll(n => n.getPluginData("generation_id") === generationId);
  for (const n of nodes) {
    n.remove();
    count++;
  }
  figma.notify("AZIA: Cleanly removed " + count + " generated nodes.");
}

async function createAnnotationOnSelection(payload) {
  const selection = figma.currentPage.selection;
  if (!selection || selection.length === 0) return;
  const target = selection[0];
  const annotation = figma.createFrame();
  annotation.name = "AZIA Annotation: " + payload.title;
  annotation.x = target.x + target.width + 24;
  annotation.y = target.y;
  annotation.resize(280, 140);
  annotation.layoutMode = "VERTICAL";
  annotation.paddingTop = 16;
  annotation.paddingBottom = 16;
  annotation.paddingLeft = 16;
  annotation.paddingRight = 16;
  annotation.itemSpacing = 8;
  annotation.cornerRadius = 8;
  annotation.fills = [{ type: "SOLID", color: { r: 1, g: 0.98, b: 0.88 } }];
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  const titleNode = figma.createText();
  titleNode.characters = "💡 " + payload.title;
  titleNode.fontSize = 12;
  titleNode.fontName = { family: "Inter", style: "Bold" };
  const descNode = figma.createText();
  descNode.characters = payload.recommendation;
  descNode.fontSize = 11;
  annotation.appendChild(titleNode);
  annotation.appendChild(descNode);
  figma.notify("Created inline UX annotation!");
}
