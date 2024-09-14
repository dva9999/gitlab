import requests
import tkinter as tk
from tkinter import ttk
from datetime import datetime


def get_actual_id(get_id):
        device_id_mapping = {  
            '72' : 'HS72_LWJRTH20TP0721458',
            '53' : 'HS53_LWJRTH20HP0721441',
            '02' : 'HS02_LWJRTH20VP0721404',
            '61' : 'HS61_LWJRTH20CP0721448',
            '13' : 'HS13_LWJRTH20PP0721414',
            '65' : 'HS65_LWJRTH20CP0721451',
            '33' : 'HS33_LWJRTH20KP0721432',
            '05' : 'HS05_LWJRTH20LP0721406',
            '31' : 'HS31_LWJRTH20TP0721430',
            '25' : 'HS25_LWJRTH20HP0721424',
            '03' : 'HS03_LWJRTH20AP0721405',
            '11' : 'HS11_LWJRTH20CP0721412',
            '69' : 'HS69_LWIRTH20HP0721455',
            '51' : 'HS51_LWJRTH20EP0721439',
            '18' : 'HS18_LWJRTH20VP0721418',
            '19' : 'HS19_LWJRTH20AP0721419',
            '58' : 'HS58_LWJRTH20PP0721445',
            '59' : 'HS59_LWJRTH20KP0721446',
            '22' : 'HS22_LWJRTH20AP0721422',
            '32' : 'HS32_LWJRTH20PP0721431',
            '16' : 'HS16_LWJRTH20JP0721416',
            '01' : 'HS01_LWJRTH20CP0721403',
            '66' : 'HS66_LWJRTH20VP0721452',
            '57' : 'HS57_LWJRTH20TP0721444',
            '60' : 'HS60_LWJRTH20JP0721447',
            '17' : 'HS17_LWJRTH20CP0721417',
            '28' : 'HS28_LWJRTH20TP0721427',
            '07' : 'HS07_LWJRTH20EP0721408',
            '39' : 'HS39_LWJRTH20LP0721437',
            '50' : 'HS50_LWJRTH20HP0721438',
            '52' : 'HS52_LWJRTH20LP0721440',
            '62' : 'HS62_LWJRTH20VP0721449',
            '29' : 'HS29_LWJRTH20PP0721428',
            '63' : 'HS63_LWJRTH20JP0721450',
            '23' : 'HS23_LWJRTH20LP0721423',
            '26' : 'HS26_LWJRTH20EP0721425',
            '08' : 'HS08_LWJRTH20CP0721409',
            '70' : 'HS70_LWJRTH20EP0721456',
            '37' : 'HS37_LWJRTH20VP0721435',
            '56' : 'HS56_LWJRTH20CP0721443',
            '15' : 'HS15_LWJRTH20KP0721415',
            '68' : 'HS68_LWJRTH20LP0721454',
            '12' : 'HS12_LWJRTH20TP0721413',
            '10' : 'HS10_LWJRTH20EP0721411',
            '55' : 'HS55_LWJRTH20EP0721442',
            '71' : 'HS71_LWJRTH20CP0721457',
            '67' : 'HS67_LWJRTH20AP0721453',
            '06' : 'HS06_LWJRTH20HP0721407',
            '36' : 'HS36_LWJRTH20CP0721434',
            '21' : 'HS21_LWJRTH20VP0721421',
            '30' : 'HS30_LWJRTH20KP0721429',
            '35' : 'HS35_LWJRTH20JP0721433',
            '38' : 'HS38_LWJRTH20AP0721436',
            '27' : 'HS27_LWJRTH20CP0721426',
            '09' : 'HS09_LWJRTH20HP0721410',
            '20' : 'HS20_LWJRTH20CP0721420',
        }
        return device_id_mapping.get(get_id)


class GetData:
    def get_file_list(self,deviceId):
        url = f"http://36.108.141.254:8090/new_mapview/api/index/GetTruckBagFileNamesList?deviceId={deviceId}"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoieXVlcGVuZyIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2dpdmVubmFtZSI6IuWys-m5jyIsIkRlcGFydG1lbnRJZCI6IjAiLCJEZXBhcnRtZW50TmFtZSI6IiIsImp0aSI6Ijg3IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmF0aW9uIjoiOS8yLzIwMjQgMTE6NDU6MzAgUE0iLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiTWFuYWdlciIsIm1hcCIsImRpc3BhdGNoIl0sIm5iZiI6MTcyNTI0ODczMCwiZXhwIjoxNzI1MjkxOTMwLCJpc3MiOiJNZXRhTWluZS5Db3JlIiwiYXVkIjoid3IifQ.svdWhyGFwD0pXTrtXQU5tKnt9UywvfiaIe3Rutxk-Hk",
            "Host": "36.108.141.254:8090",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://36.108.141.254:8090/new_mapview/?appType=0&showcamera=0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        return data


class DataHandler:
    def __init__(self, deviceId):
        self.deviceId = deviceId

    def transform_data(self, data, file_type):
        bag_files = self.filter_files(data['response'], file_type)

        for file in bag_files:
            print(file['CreationTime'])
            parts = file['BagName'].split('_')
            file['CreationTime'] = datetime.strptime(parts[3], '%Y-%m-%d-%H-%M-%S').strftime('%Y-%m-%d %H:%M:%S') #规划感知包
            #file['CreationTime'] = datetime.strptime(parts[2], '%Y-%m-%d-%H-%M-%S').strftime('%Y-%m-%d %H:%M:%S')  #定位包
        return bag_files
    
    def UploadTruckBagFile(self,file_name):
        url = f"http://36.108.141.254:8090/new_mapview/api/index/UploadTruckBagFile?deviceId={self.deviceId}&type=1"
        file_name_list = [file_name]
        response=requests.post(url, json=file_name_list)
        print(response.text)
        print(file_name_list)
    
    #创建一个函数用于筛选文件
    def filter_files(self, files, file_type):
        #print(file_type)
        #print(files)


        if file_type == "规划感知包":
            for file in files:
                if file['BagName'][0:19] == 'perception_planning' and file['BagType'] == 'Bag'  and file['BagName'][-3:] == 'bag':
                    parts = file['BagName'].split('_')
                    file['CreationTime'] = datetime.strptime(parts[3], '%Y-%m-%d-%H-%M-%S').strftime('%Y-%m-%d %H:%M:%S') #规划感知包
            return files 
        elif file_type == "定位包":
            for file in files:
                if file['BagName'][0:5] == 'local' and file['BagType'] == 'Bag'  and file['BagName'][-3:] == 'bag':
                    parts = file['BagName'].split('_')
                    file['CreationTime'] = datetime.strptime(parts[2], '%Y-%m-%d-%H-%M-%S').strftime('%Y-%m-%d %H:%M:%S')  #定位包
            return files
            #return [file for file in files if file['BagName'][0:5] == 'local' and file['BagType'] == 'Bag'  and file['BagName'][-3:] == 'bag']
        elif file_type == "控制包":
            return [file for file in files if file['BagName'][0:7] == 'control' and file['BagType'] == 'Bag'  and file['BagName'][-3:] == 'bag']
        elif file_type == "所有包":
            return [file for file in files if file['BagType'] == 'Bag'  and file['BagName'][-3:] == 'bag']
        elif file_type == "日志":
            return [file for file in files if file['BagType'] == 'Log'  and file['BagName'][-3:] == 'log']
    


class UI:
    def __init__(self, root):
        self.root = root
        self.create_ui()

    def create_ui(self):
        self.root.title("文件上传助手")
        #创建一个下拉框,用于选择上传的文件类型,默认为"规划感知包"
        self.file_type_label = tk.Label(self.root, text="文件类型:")
        self.file_type_label.pack()
        self.file_type_combobox = ttk.Combobox(self.root, values=["规划感知包", "定位包",'控制包','所有包','日志'])
        self.file_type_combobox.pack()
        self.file_type_combobox.current(0)
        #self.file_type_combobox.bind("<<ComboboxSelected>>", self.update_file_list)
        

        self.device_id_label = tk.Label(self.root, text="Device ID:")
        self.device_id_label.pack()
        #创建一个文本框，用于输入设备ID
        self.device_id_entry = tk.Entry(self.root)                                 
        self.device_id_entry.pack()
        self.device_id_entry.insert(0, "66")

        self.time_label = tk.Label(self.root, text="Time (YYYY-MM-DD HH:MM:SS):")
        self.time_label.pack()
        #创建一个文本框，用于输入时间
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack()
        #获取当前时间
        now_time = datetime.now() 
        now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')


        self.time_entry.insert(0,now_time)

        self.confirm_button = tk.Button(self.root, text="更新", command=self.update_file_list)
        self.confirm_button.pack()

        self.upload_button = tk.Button(self.root, text="上传", command=self.upload_files)  
        self.upload_button.pack()  

        self.tree = ttk.Treeview(self.root, columns=('BagName',  'BagSize', 'UploadStatus', 'CreationTime', 'Progress'), show='headings')
        #self.tree = ttk.Treeview(self.root, columns=('BagName', 'BagType', 'BagSize', 'UploadStatus', 'CreationTime', 'Progress'), show='headings')
        self.tree.heading('BagName', text='数据名称')
        #self.tree.heading('BagType', text='数据类型')
        self.tree.heading('BagSize', text='数据大小（MB）')
        self.tree.heading('UploadStatus', text='上传状态')
        self.tree.heading('CreationTime', text='创建时间')
        self.tree.heading('Progress', text='上传进度')
        self.tree.pack(expand=True, fill=tk.BOTH)

    
    def upload_files(self):
        entry_get_id = self.device_id_entry.get()
        device_id = get_actual_id(entry_get_id)

        data_handler = DataHandler(device_id)


        # 如果选择了文件，则上传选中的文件
        if self.tree.selection():
            selected_items = self.tree.selection()
            print("slected_items:",selected_items)
            for item in selected_items:
                file_name = self.tree.item(item, 'values')[0]
                data_handler.UploadTruckBagFile(file_name)
        # 如果没有选择文件，则上传列表内的第一个文件
        else:
            file_name = self.tree.item(self.tree.get_children()[0], 'values')[0]
            data_handler.UploadTruckBagFile(file_name)
        # 更新文件列表
        self.update_file_list()


    def update_file_list(self):
        entruy_get_id = self.device_id_entry.get()
        print("entruy_get_id:",entruy_get_id)
        
        device_id = get_actual_id(entruy_get_id)
        time_str = self.time_entry.get()
        time_dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')


        data_handler = DataHandler(device_id)
        get_data = GetData()

        data = get_data.get_file_list(device_id)
        #获取file_type_combobox选择的值
        file_type = self.file_type_combobox.get()
        files = data_handler.transform_data(data, file_type)

        for i in  self.tree.get_children():
            self.tree.delete(i)
        
        # 按与 time_str 的时间差排序文件
        sorted_files = sorted(files, key=lambda x: abs(datetime.strptime(x['CreationTime'], '%Y-%m-%d %H:%M:%S') - time_dt))

        
        # 获取最近的4个文件
        closest_files = sorted_files[:4]
        #对closest_files基于CreationTime进行排序
        closest_files.sort(key=lambda x: x['CreationTime'])
        






        for file  in closest_files:
            print("file:",file)
            if file['UploadStatus'] == 4:
                file['UploadStatus'] = '未上传'
            if file['UploadStatus'] == 1:
                file['UploadStatus'] = '已上传'
            if file['UploadStatus'] == 3:
                file['UploadStatus'] = '上传中'
            if file['UploadStatus'] == 5:
                file['UploadStatus'] = '上传失败'
            if file['UploadStatus'] == 2:
                file['UploadStatus'] = '等待上传'
            #self.tree.insert('', tk.END, values=(file['BagName'], file['BagType'], file['BagSize'], file['UploadStatus'], file['CreationTime'], file['Progress']))
            self.tree.insert('', tk.END, values=(file['BagName'], file['BagSize'], file['UploadStatus'], file['CreationTime'], file['Progress']))



def main():
    root = tk.Tk()
    ui = UI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
