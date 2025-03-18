import asyncio
class Asynchronous:
  async def task1(self,taskname):
    print("asynchronous")
    print(f"{taskname} started")
    await asyncio.sleep(1)
    print(f"{taskname} completed")
  async def task2(self,taskname):
    print(f"{taskname} started")
    await asyncio.sleep(1)
    print(f"{taskname} completed")
async def main():
  a=Asynchronous()
  await a.task1("task1")
  await a.task2("task2")
asyncio.run(main())