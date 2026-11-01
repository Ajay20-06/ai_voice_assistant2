from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation, silero
from livekit.plugins import openai, murf, deepgram
from livekit.plugins.google.beta import realtime

from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from tools import (
    Emergency_Call,
    Open_App,
    Take_Photo,
    Set_Volume,
    Shutdown_System,
    Restart_System,
    Type_Text,
    Move_Mouse
)

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTION,

            llm=openai.LLM(
                model="openai/gpt-oss-120b",
                base_url="https://api.groq.com/openai/v1",
                temperature=0.2,
            ),

            stt=deepgram.STT(
                model="nova-3",
                language="hi",
            ),

            tts=murf.TTS(
                voice="hi-IN-Sunaina",
                style="Conversational",
                speed=0.7,
                pitch=0
            ),

            tools=[
                Open_App,
                Take_Photo,
                Set_Volume,
                Shutdown_System,
                Restart_System,
                Type_Text,
                Move_Mouse
            ]
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession()

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC()
        )
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION
    )


if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )