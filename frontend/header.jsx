import { Play } from "lucide-react";

export default function Header() {
  return (
    <div className="h-20 border-b border-gray-800 flex items-center justify-between px-8">

      <div className="flex items-center gap-4">

        <h1 className="text-2xl font-semibold">
          Console
        </h1>

        <span className="text-yellow-500">
          TESTING
        </span>

      </div>

      <div className="flex gap-3">

        <button className="px-5 py-2 rounded bg-gray-700">
          Configure
        </button>

        <button className="bg-cyan-500 px-6 py-2 rounded flex items-center gap-2">
          <Play size={16} />
          Start Session
        </button>

      </div>

    </div>
  );
}