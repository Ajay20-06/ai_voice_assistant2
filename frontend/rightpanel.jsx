export default function RightPanel() {
  const rows = [
    "ROOM",
    "REGION",
    "DURATION",
    "PARTICIPANTS",
    "METADATA",
    "RECORDING",
    "SDK VERSION",
  ];

  return (
    <div className="w-80 border-l border-gray-800 bg-[#111317] p-5">

      <h3 className="text-gray-300 mb-5">
        SESSION
      </h3>

      {rows.map((r) => (
        <div
          key={r}
          className="border-b border-gray-700 py-4 flex justify-between"
        >
          <span className="text-gray-400">
            {r}
          </span>

          <span>—</span>

        </div>
      ))}

    </div>
  );
}