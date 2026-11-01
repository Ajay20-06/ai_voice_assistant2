import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import Console from "./components/Console";
import RightPanel from "./components/RightPanel";
import BottomTabs from "./components/BottomTabs";

export default function App() {
  return (
    <div className="h-screen bg-[#0B0B0D] text-white flex">
      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Header />

        <div className="flex flex-1 overflow-hidden">

          <div className="flex-1 p-5">

            <Console />

            <BottomTabs />

          </div>

          <RightPanel />

        </div>

      </div>
    </div>
  );
}