import time
import asyncio

# 동기/비동기 처리속도 비교 예제
## 동기 프로그래밍
def sync_task():
    time.sleep(1)
    return 'Sync Task Completed'

## 비동기 프로그래밍
async def async_task():
    await asyncio.sleep(1)
    return 'Async Task Completed'

## 동기 방식으로 작업 실행
start = time.time()
result_sync = sync_task()
end = time.time()
print('Sync Task:', result_sync)
print('Execution Time (Sync):', end - start)

## 비동기 방식으로 작업 실행
async def main():
    start = time.time()
    result_async = await async_task()
    end = time.time()
    print('Async Task:', result_async)
    print('Execution Time (Async):', end - start)

asyncio.run(main())

## 결과를 확인해보면 비동기처리가 살짝 더 빠름
Sync Task: Sync Task Completed
Execution Time (Sync): 1.0105559825897217
Async Task: Async Task Completed
Execution Time (Async): 1.0091807842254639


# 비동기 프로그래밍 예제 (비동기 함수를 사용하여 웹 페이지 내용 가져오기)
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://www.musinsa.com/ranking/best'
    content = await fetch(url)
    print(content)

asyncio.run(main())


# 서브루틴 Subroutine (동기함수 Synchronous Function)
def subroutine():
    print('subroutine')

# # 코루틴 Coroutine (비동기함수 Asynchronous Function)
async def coroutine():
    print('coroutine')