import React, { useState } from 'react';

// Design Tokens: Primary=#2563EB, Background=#F8FAFC
export default function SprintFlowWorkspaceApp() {
  const [activeScreen, setActiveScreen] = useState<string>('scr_dashboard');

  return (
    <div className="min-h-screen bg-[#F8FAFC] text-[#0F172A] font-sans antialiased flex flex-col justify-center items-center p-4">
      {/* Device Shell */}
      <div className="w-full max-w-[1280px] min-h-[900px] bg-[#FFFFFF] rounded-3xl shadow-2xl border border-[#E2E8F0] overflow-hidden flex flex-col">
        {/* Top App Bar */}
        <header className="px-6 py-4 border-b border-[#E2E8F0] flex justify-between items-center bg-[#FFFFFF]">
          <div>
            <span className="text-xs uppercase tracking-wider font-semibold text-[#64748B]">
              SprintFlow Workspace
            </span>
            <h1 className="text-lg font-bold text-[#0F172A]">
              {activeScreen}
            </h1>
          </div>
          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-[#06B6D4]/10 text-[#2563EB]">
            Live Flow
          </span>
        </header>

        {/* Dynamic Screen Viewport */}
        <main className="flex-1 p-4 overflow-y-auto space-y-4">
          {activeScreen === 'scr_dashboard' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
                <h2 className="text-base font-bold text-[#0F172A]">Sprint Engineering Dashboard</h2>
                <p className="text-xs text-[#64748B] mt-1">Provide comprehensive visibility into active sprint progress, blocker alerts, and team bandwidth.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#64748B]">Persistent Left Sidebar</h3>
                <div 
                  onClick={() => setActiveScreen('scr_kanban_board')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Global Sidebar</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
              </section>
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#64748B]">Main Dashboard View</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Sprint Burndown Metric Card</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
                <button 
                  onClick={() => setActiveScreen('scr_create_task_modal')}
                  className="w-full py-3 px-4 bg-[#2563EB] hover:bg-[#1D4ED8] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Create Task Button</span>
                </button>
              </section>
            </div>
          )}
          {activeScreen === 'scr_kanban_board' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
                <h2 className="text-base font-bold text-[#0F172A]">Agile Sprint Kanban Board</h2>
                <p className="text-xs text-[#64748B] mt-1">Visual drag-and-drop workflow tracking across Backlog, Ready, In Progress, Review, and Done columns.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#64748B]">5-Column Kanban Board</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Kanban Column: Backlog (8)</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Kanban Column: Ready for Dev (4)</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
                <div 
                  onClick={() => setActiveScreen('scr_task_detail')}
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Kanban Column: In Progress (5)</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Kanban Column: PR In Review (3)</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Kanban Column: Done & Merged (14)</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
              </section>
            </div>
          )}
          {activeScreen === 'scr_task_detail' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
                <h2 className="text-base font-bold text-[#0F172A]">Task Specification & PR Traceability Drawer</h2>
                <p className="text-xs text-[#64748B] mt-1">Inspect task acceptance criteria, assignees, linked Git branches, PR review statuses, and comments.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#64748B]">Task Detail Drawer</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Task Detail Spec</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
                <button 
                  onClick={() => setActiveScreen('scr_kanban_board')}
                  className="w-full py-3 px-4 bg-[#2563EB] hover:bg-[#1D4ED8] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Close Drawer Button</span>
                </button>
              </section>
            </div>
          )}
          {activeScreen === 'scr_analytics' && (
            <div className="space-y-4 animate-fadeIn">
              <div className="p-4 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
                <h2 className="text-base font-bold text-[#0F172A]">Sprint Velocity & Burndown Analytics</h2>
                <p className="text-xs text-[#64748B] mt-1">Visualize team velocity trends, cycle times, PR review latency, and completion forecasts.</p>
              </div>

              {/* Sections */}
              <section className="space-y-2">
                <h3 className="text-xs font-semibold uppercase text-[#64748B]">Velocity Metrics Overview</h3>
                <div 
                  
                  className="p-4 bg-[#FFFFFF] rounded-xl border border-[#E2E8F0] hover:border-[#2563EB] shadow-sm transition cursor-pointer">
                  <div className="font-semibold text-sm">Sprint Velocity Card</div>
                  <div className="text-xs text-[#64748B] mt-1">Tap to interact</div>
                </div>
                <button 
                  onClick={() => setActiveScreen('scr_kanban_board')}
                  className="w-full py-3 px-4 bg-[#2563EB] hover:bg-[#1D4ED8] text-white font-semibold rounded-xl transition duration-150 shadow-md flex items-center justify-center gap-2">
                  <span>Back to Board</span>
                </button>
              </section>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
