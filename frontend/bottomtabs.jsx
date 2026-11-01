const tabs = [
  "Audio",
  "Events",
  "Session",
  "Participants",
  "RPC",
  "DTMF",
  "Metrics",
  "Models",
];

export default function BottomTabs() {
  return (
    <div className="mt-4 border border-gray-800 rounded-xl">

      <div className="flex border-b border-gray-800">

        {tabs.map((tab, i) => (
          <button
            key={tab}
            className={`px-6 py-4 ${
              i === 0
                ? "border-b-2 border-cyan-400 text-white"
                : "text-gray-400"
            }`}
          >
            {tab}
          </button>
        ))}

      </div>

      <div className="h-52 flex items-center justify-center text-gray-500">
        Audio is only available during an active session
      </div>

    </div>
  );
}