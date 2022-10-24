# from time import sleep
# import asyncio
#
# async def downlowoad_video(photo_count):
#     while True:
#         await asyncio.sleep(1)
#         photo_count += 1
#         print(f"Photo {photo_count}...")
#
#
# async def download_video(video_count):
#     while True:
#         await asyncio.sleep(5)
#         video_count += 1
#         print(f"VIDEO {photo_count}...")
#
#
# async def main():
#     photo_count = 0
#     video_count = 0
#     task_list = [
#         download_video(photo_count)
#         download_video(video_count)
#     ]
#
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())