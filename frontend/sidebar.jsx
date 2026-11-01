import {
  LayoutDashboard,
  Bot,
  Phone,
  Settings,
  CreditCard,
  Waves,
  Monitor,
} from "lucide-react";

const menu = [
  { icon: LayoutDashboard, name: "Overview" },
  { icon: Monitor, name: "Sessions" },
  { icon: Bot, name: "Agents", active: true },
  { icon: Waves, name: "Voices" },
  { icon: Phone, name: "Telephony" },
  { icon: Settings, name: "Settings" },
  { icon: CreditCard, name: "Billing" },
];

export default function Sidebar() {
  return (
    <div className="w-72 bg-[#0F1115] border-r border-gray-800">

      <div className="text-3xl font-bold p-6">
        LiveKit
      </div>

      {menu.map((item) => (
        <div
          key={item.name}
          className={`flex items-center gap-3 px-6 py-4 cursor-pointer
          ${
            item.active
              ? "bg-cyan-900 text-cyan-300"
              : "hover:bg-gray-800"
          }`}
        >
          <item.icon size={20} />
          {item.name}
        </div>
      ))}
    </div>
  );
}