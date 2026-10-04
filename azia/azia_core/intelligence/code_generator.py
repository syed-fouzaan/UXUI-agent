"""
AZIA Production Code Generator
Converts ProductDesignSpecification into production-ready React + Tailwind CSS,
native SwiftUI, and W3C Design Token Community Group (DTCG) tokens.
"""

import json
from typing import List, Dict, Any
from azia.azia_core.models.specification import ProductDesignSpecification
from azia.azia_core.models.code_handoff import (
    FrameworkType,
    GeneratedSourceFile,
    GeneratedCodeBundle,
)


class CodeGenerator:
    """Generates production source code from design specifications."""

    def generate_react_tailwind(self, spec: ProductDesignSpecification) -> GeneratedCodeBundle:
        prod = spec.metadata
        ds = spec.design_system
        screens = spec.screens
        files: List[GeneratedSourceFile] = []

        # 1. Main App Container (App.tsx)
        app_code = f"""import React, {{ useState }} from 'react';

// Design Tokens: Primary={ds.colors.primary.hex}, Background={ds.colors.background.hex}
export default function {prod.product_name.replace(' ', '')}App() {{
  const [activeScreen, setActiveScreen] = useState<string>('{screens[0].screen_id}');

  return (
    <div className="min-h-screen bg-[{ds.colors.background.hex}] text-[{ds.colors.text_primary.hex}] font-sans antialiased flex flex-col justify-center items-center p-4">
      {{/* Device Shell */}}
      <div className="w-full max-w-[{screens[0].layout.width}px] min-h-[{screens[0].layout.height}px] bg-[{ds.colors.surface.hex}] rounded-3xl shadow-2xl border border-[{ds.colors.border_subtle.hex}] overflow-hidden flex flex-col">
        {{/* Top App Bar */}}
        <header className="px-6 py-4 border-b border-[{ds.colors.border_subtle.hex}] flex justify-between items-center bg-[{ds.colors.surface.hex}]">
          <div>
            <span className="text-xs uppercase tracking-wider font-semibold text-[{ds.colors.text_muted.hex}]">
              {prod.product_name}
            </span>
            <h1 className="text-lg font-bold text-[{ds.colors.text_primary.hex}]">
              {{activeScreen}}
            </h1>
          </div>
          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-[{ds.colors.accent.hex}]/10 text-[{ds.colors.primary.hex}]">
            Live Flow
          </span>
        </header>

        {{/* Dynamic Screen Viewport */}}
        <main className="flex-1 p-4 overflow-y-auto space-y-4">
"""
        for scr in screens:
            app_code += f"""          {{activeScreen === '{scr.screen_id}' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[{ds.colors.background.hex}] rounded-xl border border-[{ds.colors.border_subtle.hex}]">
                <h2 className="text-base font-bold text-[{ds.colors.text_primary.hex}]">{scr.screen_name}</h2>
                <p className="text-xs text-[{ds.colors.text_muted.hex}] mt-1">{scr.purpose}</p>
              </div>

              {{/* Sections */}}
"""
            for sec in scr.sections:
                app_code += f"""              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[{ds.colors.text_muted.hex}]">{sec.title}</h3>
"""
                for cmp in sec.components:
                    target = cmp.interactive_target_screen_id or scr.prototype_destinations.get(cmp.instance_id, "")
                    nav_action = f"onClick={{() => setActiveScreen('{target}')}}" if target else ""
                    if "btn" in cmp.component_ref:
                        app_code += f"""                <button 
                  {nav_action}
                  className="w-full py-3 px-4 bg-[{ds.colors.primary.hex}] hover:bg-[{ds.colors.primary_hover.hex}] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>{cmp.name}</span>
                </button>
"""
                    else:
                        app_code += f"""                <div 
                  {nav_action}
                  className="p-4 bg-[{ds.colors.surface.hex}] rounded-xl border border-[{ds.colors.border_subtle.hex}] hover:border-[{ds.colors.primary.hex}] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">{cmp.name}</div>
                  <div className="text-xs text-[{ds.colors.text_muted.hex}] mt-1">Tap to interact</div>
                </div>
"""
                app_code += "              </section>\n"
            app_code += "            </div>\n          )}\n"

        app_code += """        </main>
      </div>
    </div>
  );
}
"""
        files.append(GeneratedSourceFile(
            filename="App.tsx",
            relative_path="src/App.tsx",
            language="tsx",
            description="Complete interactive React component with Tailwind CSS styling and Auto Layout structures.",
            code_content=app_code
        ))

        # 2. Tailwind Config theme extension
        tailwind_config = f"""/** @type {{import('tailwindcss').Config}} */
module.exports = {{
  content: ["./src/**/*.{{js,ts,jsx,tsx}}"],
  theme: {{
    extend: {{
      colors: {{
        primary: '{ds.colors.primary.hex}',
        'primary-hover': '{ds.colors.primary_hover.hex}',
        secondary: '{ds.colors.secondary.hex}',
        accent: '{ds.colors.accent.hex}',
        background: '{ds.colors.background.hex}',
        surface: '{ds.colors.surface.hex}',
        border: '{ds.colors.border_subtle.hex}',
      }},
      fontFamily: {{
        sans: ['Inter', 'system-ui', 'sans-serif'],
      }},
    }},
  }},
  plugins: [],
}};
"""
        files.append(GeneratedSourceFile(
            filename="tailwind.config.js",
            relative_path="tailwind.config.js",
            language="javascript",
            description="Tailwind CSS theme config mapped directly from AZIA Design System tokens.",
            code_content=tailwind_config
        ))

        return GeneratedCodeBundle(
            product_name=prod.product_name,
            framework=FrameworkType.REACT_TAILWIND,
            files=files,
            install_instructions="npm install react react-dom lucide-react\nnpm install -D tailwindcss postcss autoprefixer",
            package_dependencies=["react", "react-dom", "lucide-react", "tailwindcss"]
        )

    def generate_swiftui(self, spec: ProductDesignSpecification) -> GeneratedCodeBundle:
        prod = spec.metadata
        ds = spec.design_system
        screens = spec.screens
        files: List[GeneratedSourceFile] = []

        swift_code = f"""//
//  {prod.product_name.replace(' ', '')}App.swift
//  Generated autonomously by AZIA • Autonomous Figma Product Design MCP
//

import SwiftUI

struct {prod.product_name.replace(' ', '')}App: App {{
    var body: some Scene {{
        WindowGroup {{
            ContentView()
        }}
    }}
}}

struct ContentView: View {{
    @State private var selectedScreen: String = "{screens[0].screen_id}"

    // Design Tokens
    let primaryColor = Color(hex: "{ds.colors.primary.hex}")
    let backgroundColor = Color(hex: "{ds.colors.background.hex}")
    let surfaceColor = Color(hex: "{ds.colors.surface.hex}")

    var body: some View {{
        NavigationStack {{
            ZStack {{
                backgroundColor.ignoresSafeArea()

                VStack(spacing: 16) {{
                    // Screen Title Header
                    VStack(alignment: .leading, spacing: 4) {{
                        Text("{prod.product_name.upper()}")
                            .font(.caption)
                            .fontWeight(.bold)
                            .foregroundColor(.secondary)
                        Text(selectedScreen)
                            .font(.title2)
                            .fontWeight(.bold)
                    }}
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .padding(.horizontal)

                    ScrollView {{
                        VStack(spacing: 16) {{
"""
        for scr in screens:
            swift_code += f"""                            if selectedScreen == "{scr.screen_id}" {{
                                // Screen: {scr.screen_name}
                                VStack(alignment: .leading, spacing: 12) {{
                                    Text("{scr.purpose}")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {{
                                        // Navigate to next
                                    }}) {{
                                        Text("{scr.primary_cta}")
                                            .font(.headline)
                                            .foregroundColor(.white)
                                            .frame(maxWidth: .infinity)
                                            .padding()
                                            .background(primaryColor)
                                            .cornerRadius(12)
                                    }}
                                }}
                                .padding()
                                .background(surfaceColor)
                                .cornerRadius(16)
                                .shadow(color: Color.black.opacity(0.05), radius: 8, x: 0, y: 2)
                            }}
"""

        swift_code += """                        }
                        .padding(.horizontal)
                    }
                }
            }
        }
    }
}

// Color Hex Extension
extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 6: // RGB
            (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        default:
            (a, r, g, b) = (255, 0, 0, 0)
        }
        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue: Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
}
"""
        files.append(GeneratedSourceFile(
            filename="ContentView.swift",
            relative_path="Sources/ContentView.swift",
            language="swift",
            description="Native SwiftUI multi-screen view with Auto Layout stack mappings and hex color extensions.",
            code_content=swift_code
        ))

        return GeneratedCodeBundle(
            product_name=prod.product_name,
            framework=FrameworkType.SWIFTUI,
            files=files,
            install_instructions="Open project in Xcode 15+ and run on iOS 17+ Simulator.",
            package_dependencies=[]
        )

    def generate_w3c_tokens(self, spec: ProductDesignSpecification) -> GeneratedSourceFile:
        """Generates W3C Design Tokens Community Group (DTCG) standard tokens.json."""
        ds = spec.design_system
        dtcg = {
            "$schema": "https://design-tokens.github.io/community-group/format/",
            "color": {
                "primary": {"$value": ds.colors.primary.hex, "$type": "color"},
                "secondary": {"$value": ds.colors.secondary.hex, "$type": "color"},
                "accent": {"$value": ds.colors.accent.hex, "$type": "color"},
                "background": {"$value": ds.colors.background.hex, "$type": "color"},
                "surface": {"$value": ds.colors.surface.hex, "$type": "color"},
                "text": {"$value": ds.colors.text_primary.hex, "$type": "color"},
                "border": {"$value": ds.colors.border_subtle.hex, "$type": "color"},
            },
            "spacing": {
                "sm": {"$value": f"{ds.spacing.sm}px", "$type": "dimension"},
                "md": {"$value": f"{ds.spacing.md}px", "$type": "dimension"},
                "lg": {"$value": f"{ds.spacing.lg}px", "$type": "dimension"},
                "xl": {"$value": f"{ds.spacing.xl}px", "$type": "dimension"},
            },
            "radius": {
                "sm": {"$value": f"{ds.radius.sm}px", "$type": "dimension"},
                "md": {"$value": f"{ds.radius.md}px", "$type": "dimension"},
                "full": {"$value": f"{ds.radius.full}px", "$type": "dimension"},
            }
        }

        return GeneratedSourceFile(
            filename="tokens.json",
            relative_path="tokens/tokens.json",
            language="json",
            description="W3C Design Token Community Group (DTCG) specification.",
            code_content=json.dumps(dtcg, indent=2)
        )
