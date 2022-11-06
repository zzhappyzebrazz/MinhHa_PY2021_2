class NhanVien:
    '''
    Class NhanVien
    '''
    def __init__(self, ho_ten, he_so_luong, gia_canh, thu_lao):
        print('ctor NhanVien')
        self.ho_ten = ho_ten
        self.he_so_luong = he_so_luong
        self.gia_canh = gia_canh
        self.thu_lao = thu_lao
        self.luong_cb = 1600000
        
    def tinh_luong(self):
        self.tn_truoc_thue = self.he_so_luong * self.luong_cb + self.thu_lao
        
        self.tn_chiu_thue = self.tn_truoc_thue - 11000000 - (self.gia_canh * 4400000)
        
        if self.tn_chiu_thue < 5000000:
            self.thue_TNCN = self.tn_chiu_thue * 0.05

        elif self.tn_chiu_thue >= 5000000 and self.tn_chiu_thue < 10000000:
            self.thue_TNCN = self.tn_chiu_thue * 0.1 - 250000
        
        elif self.tn_chiu_thue >= 10000000 and self.tn_chiu_thue < 18000000:
            self.thue_TNCN = self.tn_chiu_thue * 0.15 - 750000
            
        elif self.tn_chiu_thue >= 18000000 and self.tn_chiu_thue < 32000000:
            self.thue_TNCN = self.tn_chiu_thue * 0.20 - 1650000

        elif self.tn_chiu_thue >= 32000000 and self.tn_chiu_thue < 52000000:
            self.thue_TNCN = self.tn_chiu_thue * 0.25 - 3250000
            
        elif self.tn_chiu_thue >= 52000000 and self.tn_chiu_thue < 80000000:
            self.thue_TNCN = self.tn_chiu_thue * 0.30 - 5850000
        
        else:
            self.thue_TNCN = self.tn_chiu_thue * 0.35 - 9850000

        self.tn_sau_thue = self.tn_truoc_thue - self.thue_TNCN
        
    def ket_qua(self):
        print(f'Thu nhập trước thuế: {self.tn_truoc_thue:,}')
        print(f'Thu nhập chịu thuế: {self.tn_chiu_thue:,}')
        print(f'Thuế thu nhập cá nhân: {self.thue_TNCN:,}')
        print(f'Thực lĩnh: {self.tn_sau_thue:,}')
        
    def __del__(self):
        print("Dtor NhanVien")
        pass
    
    def __str__(self):
        result = "Họ và tên: " + self.ho_ten + '\n'
        result += "Hệ số lương: " + str(self.he_so_luong) + '\n'
        result += "Số người giảm trừ gia cảnh: " + str(self.gia_canh) + '\n'
        result += "Thu lao trong tháng: " + str(self.thu_lao) + '\n'
        result += "Lương cơ bản: " + str(self.luong_cb) + '\n'
        result += "Thu nhận trước thuế: " + str(self.tn_truoc_thue) + '\n'
        result += "Thu nhập chịu thuế: " + str(self.tn_chiu_thue) + '\n'
        result += "Thuế thu nhập cá nhân: " + str(self.thue_TNCN) + '\n'
        result += "Thu nhập sau thuế: " + str(self.tn_sau_thue) + '\n'
        return result

# class QuanLyNhanVien:
#     '''
#     class QuanLyNhanVien
#     '''
#     def __init__(self):
        

def main():
    nv = NhanVien('Lại Minh Hà', 2.67, 1, 12000000)
    nv.tinh_luong()
    nv.ket_qua()
    # print(nv)
    
if __name__ == "__main__":
    main()
        