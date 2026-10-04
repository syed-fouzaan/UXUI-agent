import React, { useState } from 'react';

// Design Tokens: Primary=#EA580C, Background=#FAFAF9
export default function CraveBiteCampusApp() {
  const [activeScreen, setActiveScreen] = useState<string>('scr_home');

  return (
    <div className="min-h-screen bg-[#FAFAF9] text-[#1C1917] font-sans antialiased flex flex-col justify-center items-center p-4">
      {/* Device Shell */}
      <div className="w-full max-w-[393px] min-h-[852px] bg-[#FFFFFF] rounded-3xl shadow-2xl border border-[#E7E5E4] overflow-hidden flex flex-col">
        {/* Top App Bar */}
        <header className="px-6 py-4 border-b border-[#E7E5E4] flex justify-between items-center bg-[#FFFFFF]">
          <div>
            <span className="text-xs uppercase tracking-wider font-semibold text-[#78716C]">
              CraveBite Campus
            </span>
            <h1 className="text-lg font-bold text-[#1C1917]">
              {activeScreen}
            </h1>
          </div>
          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-[#F59E0B]/10 text-[#EA580C]">
            Live Flow
          </span>
        </header>

        {/* Dynamic Screen Viewport */}
        <main className="flex-1 p-4 overflow-y-auto space-y-4">
          {activeScreen === 'scr_home' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#FAFAF9] rounded-xl border border-[#E7E5E4]">
                <h2 className="text-base font-bold text-[#1C1917]">Campus Discovery & Feed</h2>
                <p className="text-xs text-[#78716C] mt-1">Present campus dining spots, flash student budget deals, and immediate search affordance.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Dorm Delivery Location & Search</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Delivery Address Bar</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  onClick={() => setActiveScreen('scr_search')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Global Search Input</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Student Saver Quick Filters</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Filter Pill: Under $10 💰</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Filter Pill: ⚡ Under 20 Mins</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Filter Pill: 🌱 Plant-Based</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Filter Pill: Late Night 🌙</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Filter Pill: Top Rated ⭐</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Fast & Nearby Campus Favorites</h3>
                <div 
                  onClick={() => setActiveScreen('scr_restaurant_detail')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Restaurant Card: Quad Noodle Bar & Dumplings</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  onClick={() => setActiveScreen('scr_restaurant_detail')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Restaurant Card: Varsity Burrito Co.</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  onClick={() => setActiveScreen('scr_restaurant_detail')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Restaurant Card: Library Street Woodfired Pizza</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
            </div>
          )}
          {activeScreen === 'scr_search' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#FAFAF9] rounded-xl border border-[#E7E5E4]">
                <h2 className="text-base font-bold text-[#1C1917]">Dietary Search & Query Results</h2>
                <p className="text-xs text-[#78716C] mt-1">Allow granular filtering by price, prep speed, and campus building drop point.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Query Input with Back Button</h3>
                <div 
                  onClick={() => setActiveScreen('scr_home')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Back Arrow</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Focused Search Input</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Matched Meals Under $10</h3>
                <div 
                  onClick={() => setActiveScreen('scr_restaurant_detail')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Result Card: Crispy Garlic Noodles</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
            </div>
          )}
          {activeScreen === 'scr_restaurant_detail' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#FAFAF9] rounded-xl border border-[#E7E5E4]">
                <h2 className="text-base font-bold text-[#1C1917]">Restaurant Menu & Customizer</h2>
                <p className="text-xs text-[#78716C] mt-1">Explore restaurant menu sections and customize toppings, spice levels, and portions.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Restaurant Hero & Info</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Restaurant Metadata Box</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Popular Student Combos</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Dish Item: Garlic Noodles</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Floating Cart Summary Bar</h3>
                <button 
                  onClick={() => setActiveScreen('scr_cart')}
                  className="w-full py-3 px-4 bg-[#EA580C] hover:bg-[#C2410C] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>View Cart (2 Items) • $11.99</span>
                </button>
              </section>
            </div>
          )}
          {activeScreen === 'scr_cart' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#FAFAF9] rounded-xl border border-[#E7E5E4]">
                <h2 className="text-base font-bold text-[#1C1917]">Cart & Student Discount Review</h2>
                <p className="text-xs text-[#78716C] mt-1">Review item quantities, apply promo codes, select campus landmark drop point.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Your Order from Quad Noodle Bar</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Cart Item: Crispy Chili Garlic Noodles</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Cart Item: Pan-Fried Gyoza (4 pcs)</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Campus Pickup Landmark</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Dorm Drop Point</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Student Pricing Breakdown</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Bill Summary Box</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <button 
                  onClick={() => setActiveScreen('scr_checkout')}
                  className="w-full py-3 px-4 bg-[#EA580C] hover:bg-[#C2410C] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Checkout Button</span>
                </button>
              </section>
            </div>
          )}
          {activeScreen === 'scr_checkout' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#FAFAF9] rounded-xl border border-[#E7E5E4]">
                <h2 className="text-base font-bold text-[#1C1917]">Frictionless Payment & Confirmation</h2>
                <p className="text-xs text-[#78716C] mt-1">One-tap payment authorization via Apple Pay, Student Campus ID Card, or Credit Card.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Payment Method</h3>
                <button 
                  
                  className="w-full py-3 px-4 bg-[#EA580C] hover:bg-[#C2410C] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Apple Pay Option</span>
                </button>
                <button 
                  
                  className="w-full py-3 px-4 bg-[#EA580C] hover:bg-[#C2410C] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Campus ID Cash Option</span>
                </button>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Final Authorize Order</h3>
                <button 
                  onClick={() => setActiveScreen('scr_order_confirmation')}
                  className="w-full py-3 px-4 bg-[#EA580C] hover:bg-[#C2410C] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Confirm and Pay Button</span>
                </button>
              </section>
            </div>
          )}
          {activeScreen === 'scr_order_confirmation' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#FAFAF9] rounded-xl border border-[#E7E5E4]">
                <h2 className="text-base font-bold text-[#1C1917]">Order Confirmed & Kitchen Ticket</h2>
                <p className="text-xs text-[#78716C] mt-1">Provide immediate peace of mind, order number, kitchen prep timer, and tracking shortcut.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Success Confirmation</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Order Placed Badge</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Prep Time Summary</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <button 
                  onClick={() => setActiveScreen('scr_order_tracking')}
                  className="w-full py-3 px-4 bg-[#EA580C] hover:bg-[#C2410C] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Live Track Delivery Button</span>
                </button>
              </section>
            </div>
          )}
          {activeScreen === 'scr_order_tracking' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#FAFAF9] rounded-xl border border-[#E7E5E4]">
                <h2 className="text-base font-bold text-[#1C1917]">Live Campus Delivery Map & PIN</h2>
                <p className="text-xs text-[#78716C] mt-1">Display real-time GPS location of courier on campus pathways, ETA, and 4-digit pickup security PIN.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#78716C]">Campus Courier Map View</h3>
                <div 
                  onClick={() => setActiveScreen('scr_home')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E7E5E4] hover:border-[#EA580C] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Live Campus Map Simulator</div>
                  <div className="text-xs text-[#78716C] mt-1">Tap to interact</div>
                </div>
                <button 
                  
                  className="w-full py-3 px-4 bg-[#EA580C] hover:bg-[#C2410C] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Contact Courier Button</span>
                </button>
              </section>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
