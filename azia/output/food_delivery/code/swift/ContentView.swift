//
//  CraveBiteCampusApp.swift
//  Generated autonomously by AZIA • Autonomous Figma Product Design MCP
//

import SwiftUI

struct CraveBiteCampusApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    @State private var selectedScreen: String = "scr_home"

    // Design Tokens
    let primaryColor = Color(hex: "#EA580C")
    let backgroundColor = Color(hex: "#FAFAF9")
    let surfaceColor = Color(hex: "#FFFFFF")

    var body: some View {
        NavigationStack {
            ZStack {
                backgroundColor.ignoresSafeArea()

                VStack(spacing: 16) {
                    // Screen Title Header
                    VStack(alignment: .leading, spacing: 4) {
                        Text("CRAVEBITE CAMPUS")
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
                            if selectedScreen == "scr_home" {
                                // Screen: Campus Discovery & Feed
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Present campus dining spots, flash student budget deals, and immediate search affordance.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Explore Student Deals")
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
                            if selectedScreen == "scr_search" {
                                // Screen: Dietary Search & Query Results
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Allow granular filtering by price, prep speed, and campus building drop point.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Apply 2 Filters")
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
                            if selectedScreen == "scr_restaurant_detail" {
                                // Screen: Restaurant Menu & Customizer
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Explore restaurant menu sections and customize toppings, spice levels, and portions.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Add to Order • $8.49")
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
                            if selectedScreen == "scr_cart" {
                                // Screen: Cart & Student Discount Review
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Review item quantities, apply promo codes, select campus landmark drop point.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Proceed to Checkout • $10.34")
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
                            if selectedScreen == "scr_checkout" {
                                // Screen: Frictionless Payment & Confirmation
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("One-tap payment authorization via Apple Pay, Student Campus ID Card, or Credit Card.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Slide to Pay • $10.34")
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
                            if selectedScreen == "scr_order_confirmation" {
                                // Screen: Order Confirmed & Kitchen Ticket
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Provide immediate peace of mind, order number, kitchen prep timer, and tracking shortcut.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Live Track Delivery")
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
                            if selectedScreen == "scr_order_tracking" {
                                // Screen: Live Campus Delivery Map & PIN
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Display real-time GPS location of courier on campus pathways, ETA, and 4-digit pickup security PIN.")
                                        .font(.subheadline)
                                        .foregroundColor(.secondary)

                                    Button(action: {
                                        // Navigate to next
                                    }) {
                                        Text("Message Courier")
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
