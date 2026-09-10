import csv

class Work:
    def __init__(self,name,time,status):
        self.name = name
        self.time = time
        self.status = status

    def is_done(self):
        if self.status == "done":
            return True
        else:
            return False

def load_works():
    works = []
    has_error = False
    count = 0
    error_count = []

    try:
        with open("work.csv","r",newline="",encoding="utf-8") as file:
            reader = csv.reader(file)
            
            for row in reader:
                error_detail={"gyo":None,"detail":None,"row":None}
                count += 1
                try:
                    work = Work(row[0],int(row[1]),row[2])
                    works.append(work)
                except ValueError as e:
                    print(f"値が整数ではありません：{e}")
                    has_error = True
                    error_detail["gyo"] = count
                    error_detail["detail"] = f"値が整数ではありません：{e}"
                    error_detail["row"] = row
                    error_count.append(error_detail)
                except IndexError as e:
                    print(f"値が足りません：{e}")
                    has_error = True
                    error_detail["gyo"] = count
                    error_detail["detail"] = f"値が足りません：{e}"
                    error_detail["row"] = row
                    error_count.append(error_detail)

    except FileNotFoundError as e:
        print(f"ファイルがありません：{e}")
        has_error = True    
    
    return works,has_error,error_count

def done_count(works):
    count = 0
    for work in works:
        if work.is_done():
            count += 1
    return count

def done_total(works):
    total = 0
    for work in works:
        if work.is_done():
            total += work.time
    return total

def longest_done_time(works):
    longest = 0
    for work in works:
        if work.is_done():
            if longest < work.time:
                longest = work.time
    return longest

works ,has_error,error_detailes = load_works()

if has_error:
    print("データに不具合があったため中断します")
    for error_detail in error_detailes:
        print(f"エラー行：{error_detail['gyo']}")
        print(f"エラー詳細：{error_detail['detail']}")
        print(f"エラーデータ：{error_detail['row']}")
else:
    print(f"done件数{done_count(works)}")
    print(f"done合計時間{done_total(works)}")
    print(f"done最長時間{longest_done_time(works)}")
    
    