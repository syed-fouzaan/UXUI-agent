//
//  SprintFlowWorkspaceApp.swift
//  Generated autonomously by AZIA • Autonomous Figma Product Design MCP
//

import SwiftUI

struct SprintFlowWorkspaceApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    @State private var selectedScreen: String = "scr_dashboard"

    // Design Tokens
    let primaryColor = Color(hex: "#2563EB")
    let backgroundColor = Color(hex: "#F8FAFC")
    let surfaceColor = Color(hex: "#FFFFFF")

    var body: some View {
        NavigationStack {
            ZStack {
                backgroundColor.ignoresSafeArea()

                VStack(spacing: 16) {
                    // Screen Title Header
                    VStack(alignment: .leading, spacing: 4) {
                        Text("SPRINTFLOW WORKSPACE")
                            .font(.caption)
                            .fontWeight(.bold)
                            .foregroundColor(.secondary)
                        Text(selectedScreen)
                            .font(.title2)
                            .fontWeight(.bold)
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .padding(.horizontal)

                    ScrollView {
                        VStack(spacing: 16) {
                            if selectedScreen == "scr_dashboard" {
                                // Screen: Sprint Engineering Dashboard
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Provide comprehensive visibility into active sprint progress, blocker alerts, and team bandwidth.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("+ New Task (C)")
                                            .font(.headline)
                                            .foregroundColor(.white)
                                            .frame(maxWidth: .infinity)
                                            .padding()
                                            .background(primaryColor)
                                            .cornerRadius(12)
                                    }
                                }
                                .padding()
                                .background(surfaceColor)
                                .cornerRadius(16)
                                .shadow(color: Color.black.opacity(0.05), radius: 8, x: 0, y: 2)
                            }
                            if selectedScreen == "scr_kanban_board" {
                                // Screen: Agile Sprint Kanban Board
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Visual drag-and-drop workflow tracking across Backlog, Ready, In Progress, Review, and Done columns.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("+ Add Task to Column")
                                            .font(.headline)
                                            .foregroundColor(.white)
                                            .frame(maxWidth: .infinity)
                                            .padding()
                                            .background(primaryColor)
                                            .cornerRadius(12)
                                    }
                                }
                                .padding()
                                .background(surfaceColor)
                                .cornerRadius(16)
                                .shadow(color: Color.black.opacity(0.05), radius: 8, x: 0, y: 2)
                            }
                            if selectedScreen == "scr_task_detail" {
                                // Screen: Task Specification & PR Traceability Drawer
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Inspect task acceptance criteria, assignees, linked Git branches, PR review statuses, and comments.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Move to PR In Review")
                                            .font(.headline)
                                            .foregroundColor(.white)
                                            .frame(maxWidth: .infinity)
                                            .padding()
                                            .background(primaryColor)
                                            .cornerRadius(12)
                                    }
                                }
                                .padding()
                                .background(surfaceColor)
                                .cornerRadius(16)
                                .shadow(color: Color.black.opacity(0.05), radius: 8, x: 0, y: 2)
                            }
                            if selectedScreen == "scr_analytics" {
                                // Screen: Sprint Velocity & Burndown Analytics
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Visualize team velocity trends, cycle times, PR review latency, and completion forecasts.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Export Retrospective PDF")
                                            .font(.headline)
                                            .foregroundColor(.white)
                                            .frame(maxWidth: .infinity)
                                            .padding()
                                            .background(primaryColor)
                                            .cornerRadius(12)
                                    }
                                }
                                .padding()
                                .background(surfaceColor)
                                .cornerRadius(16)
                                .shadow(color: Color.black.opacity(0.05), radius: 8, x: 0, y: 2)
                            }
                        }
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
