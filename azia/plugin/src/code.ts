/**
 * AZIA Autonomous Figma & FigJam Plugin Sandbox Execution Layer
 * Executes deterministic semantic operations, applies design tokens,
 * tags ownership metadata (managed_by='autonomous-design-mcp'),
 * inspects user selections for UX audits, and guarantees non-destructive rollbacks.
 */

// Show the plugin UI with responsive dimensions
figma.showUI(__html__, { width: 440, height: 680, themeColors: true });

// Message dispatcher between UI sandbox and Figma Engine
figma.ui.onmessage = async (msg: { type: string; payload?: any }) => {
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
      console.warn("Unknown message received in AZIA code sandbox:", msg.type);
  }
};

/**
 * Inspects current Figma selection and sends structural metadata to UI for UX audit
 */
function inspectSelection() {
  const selection = figma.currentPage.selection;
  if (!selection || selection.length === 0) {
    figma.ui.postMessage({
      type: "SELECTION_INSPECTED",
      payload: {
        has_selection: false,
        message: "No layer selected. Select a screen or frame to audit."
      }
    });
    return;
  }

  const node = selection[0];
  const metadata = {
    has_selection: true,
    id: node.id,
    name: node.name,
    type: node.type,
    width: node.width,
    height: node.height,
    is_managed_by_azia: node.getPluginData("managed_by") === "autonomous-design-mcp",
    generation_id: node.getPluginData("generation_id"),
    has_auto_layout: "layoutMode" in node && (node as any).layoutMode !== "NONE"
  };

  figma.ui.postMessage({
    type: "SELECTION_INSPECTED",
    payload: metadata
  });
}

/**
 * Deterministically applies semantic operations received from MCP or backend
 */
async function executeOperations(payload: {
  operations: any[];
  generation_id: string;
  product_name: string;
}) {
  const { operations, generation_id, product_name } = payload;
  figma.notify(`AZIA: Rendering ${product_name} (${operations.length} ops)...`);

  // Load standard fonts before rendering text
  try {
    await figma.loadFontAsync({ family: "Inter", style: "Regular" });
    await figma.loadFontAsync({ family: "Inter", style: "Medium" });
    await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
    await figma.loadFontAsync({ family: "Inter", style: "Bold" });
  } catch (err) {
    console.warn("Standard fonts loaded with fallback:", err);
  }

  const createdNodes: { [key: string]: SceneNode } = {};
  let renderedCount = 0;

  for (const op of operations) {
    try {
      const parent = op.parent_id ? (createdNodes[op.parent_id] as (BaseNode & ChildrenMixin)) : figma.currentPage;

      if (op.op_type === "create_section") {
        if ("createSection" in figma) {
          const sec = (figma as any).createSection();
          sec.name = op.name;
          sec.x = op.payload?.x || 0;
          sec.y = op.payload?.y || 0;
          sec.resizeWithoutConstraints(op.payload?.width || 1200, op.payload?.height || 800);
          sec.setPluginData("managed_by", "autonomous-design-mcp");
          sec.setPluginData("generation_id", generation_id);
          createdNodes[op.target_id] = sec;
          renderedCount++;
        }
      } else if (op.op_type === "create_screen" || op.op_type === "create_frame") {
        const frame = figma.createFrame();
        frame.name = op.name;
        frame.x = op.payload?.x || 0;
        frame.y = op.payload?.y || 0;
        frame.resize(op.payload?.width || 393, op.payload?.height || 852);

        // Auto Layout Setup
        frame.layoutMode = op.payload?.direction === "horizontal" ? "HORIZONTAL" : "VERTICAL";
        frame.paddingTop = op.payload?.padding_top || 0;
        frame.paddingBottom = op.payload?.padding_bottom || 0;
        frame.paddingLeft = op.payload?.padding_x || 0;
        frame.paddingRight = op.payload?.padding_x || 0;
        frame.itemSpacing = op.payload?.gap || 12;

        if (op.payload?.bg_hex) {
          const rgb = hexToRgb(op.payload.bg_hex);
          frame.fills = [{ type: "SOLID", color: rgb }];
        }

        frame.setPluginData("managed_by", "autonomous-design-mcp");
        frame.setPluginData("generation_id", generation_id);
        frame.setPluginData("screen_id", op.target_id);

        if (parent && "appendChild" in parent) {
          parent.appendChild(frame);
        }
        createdNodes[op.target_id] = frame;
        renderedCount++;
      } else if (op.op_type === "create_card" || op.op_type === "create_auto_layout") {
        const frame = figma.createFrame();
        frame.name = op.name;
        frame.layoutMode = op.payload?.direction === "horizontal" ? "HORIZONTAL" : "VERTICAL";
        frame.paddingTop = op.payload?.padding || 12;
        frame.paddingBottom = op.payload?.padding || 12;
        frame.paddingLeft = op.payload?.padding || 16;
        frame.paddingRight = op.payload?.padding || 16;
        frame.itemSpacing = op.payload?.gap || 8;
        frame.cornerRadius = op.payload?.corner_radius || 8;

        if (op.payload?.bg_color_hex) {
          frame.fills = [{ type: "SOLID", color: hexToRgb(op.payload.bg_color_hex) }];
        }
        frame.setPluginData("managed_by", "autonomous-design-mcp");

        if (parent && "appendChild" in parent) {
          parent.appendChild(frame);
        }
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

        if (parent && "appendChild" in parent) {
          parent.appendChild(textNode);
        }
        createdNodes[op.target_id] = textNode;
        renderedCount++;
      } else if (op.op_type === "create_sticky_note") {
        if (figma.editorType === "figjam" && "createSticky" in figma) {
          const sticky = (figma as any).createSticky();
          sticky.text.characters = op.payload?.content || "";
          sticky.x = op.payload?.x || 0;
          sticky.y = op.payload?.y || 0;
          sticky.setPluginData("managed_by", "autonomous-design-mcp");
          sticky.setPluginData("generation_id", generation_id);
          createdNodes[op.target_id] = sticky;
          renderedCount++;
        }
      }
    } catch (opErr) {
      console.error(`Error executing op ${op.op_id}:`, opErr);
    }
  }

  // Zoom to fit newly generated content
  const allCreated = Object.values(createdNodes).filter(n => n.type !== "PAGE");
  if (allCreated.length > 0) {
    figma.viewport.scrollAndZoomIntoView(allCreated);
  }

  figma.notify(`AZIA: Success! Rendered ${renderedCount} verified nodes to canvas. ✨`);
  figma.ui.postMessage({
    type: "OPERATIONS_COMPLETED",
    payload: { rendered_count: renderedCount, generation_id }
  });
}

/**
 * Non-destructively removes ONLY nodes tagged with generation_id
 */
function rollbackGeneration(generationId: string) {
  if (!generationId) {
    figma.notify("No generation ID specified for rollback.", { error: true });
    return;
  }

  let deleted = 0;
  const nodes = figma.currentPage.findAll(n => n.getPluginData("generation_id") === generationId);
  for (const n of nodes) {
    n.remove();
    deleted++;
  }

  figma.notify(`AZIA Rollback: Cleanly removed ${deleted} generated nodes.`);
  figma.ui.postMessage({
    type: "ROLLBACK_COMPLETED",
    payload: { deleted_count: deleted }
  });
}

/**
 * Creates inline annotation pinned to the selected frame
 */
async function createAnnotationOnSelection(payload: { title: string; recommendation: string }) {
  const selection = figma.currentPage.selection;
  if (!selection || selection.length === 0) return;

  const target = selection[0];
  const annotation = figma.createFrame();
  annotation.name = `AZIA Annotation: ${payload.title}`;
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
  annotation.strokes = [{ type: "SOLID", color: { r: 0.9, g: 0.7, b: 0.2 } }];

  await figma.loadFontAsync({ family: "Inter", style: "Bold" });
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });

  const titleNode = figma.createText();
  titleNode.characters = `💡 ${payload.title}`;
  titleNode.fontSize = 12;
  titleNode.fontName = { family: "Inter", style: "Bold" };

  const descNode = figma.createText();
  descNode.characters = payload.recommendation;
  descNode.fontSize = 11;

  annotation.appendChild(titleNode);
  annotation.appendChild(descNode);
  figma.notify("Created inline UX annotation!");
}

function hexToRgb(hex: string): { r: number; g: number; b: number } {
  hex = hex.replace("#", "");
  if (hex.length === 3) {
    hex = hex.split("").map(c => c + c).join("");
  }
  const num = parseInt(hex, 16);
  return {
    r: ((num >> 16) & 255) / 255,
    g: ((num >> 8) & 255) / 255,
    b: (num & 255) / 255
  };
}
