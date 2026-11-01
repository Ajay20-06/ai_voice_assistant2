import { Bot } from "lucide-react";

export default function Console() {
  return (
    <div className="bg-[#111317] border border-gray-800 rounded-xl h-[430px] flex flex-col justify-center items-center">

      <Bot size={60} className="text-gray-500" />

      <h2 className="text-3xl mt-6 font-bold">
        Test your agent
      </h2>

      <p className="text-gray-400 mt-3 text-center max-w-xl">
        Console is the fastest way to monitor, test and debug your
        AI agent with transcripts, events and metrics.
      </p>

      <div className="flex gap-4 mt-8">

        <button className="bg-gray-700 px-5 py-3 rounded">
          Open Console Configuration
        </button>

        <button className="bg-cyan-500 px-6 py-3 rounded">
          Start Session
        </button>

      </div>

    </div>
  );
}