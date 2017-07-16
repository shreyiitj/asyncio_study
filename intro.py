
import asyncio
from asyncio import coroutine
import time


@coroutine
def func1():
	print("in func1")
	yield from asyncio.sleep(2)	# not cpu bounded and time consuming
	print("func1 done")

@coroutine
def func2():
	print("in func2")
	yield from asyncio.sleep(2)	# not cpu bounded and time consuming
	print("func2 done")

@coroutine				
def main():				# main funciton which controls everything
	print("in main")
	yield from func1()
	yield from func2()
	
@coroutine
def main2():
	tasks = [func1(),func2()]
	obj = asyncio.gather(*tasks)
	return obj


start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# loop.run_until_complete(main2)
loop.close()
end = time.time()
print("it took ", str(end - start))

