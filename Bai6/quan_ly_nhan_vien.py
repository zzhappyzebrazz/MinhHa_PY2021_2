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
            self.thue_TNCN = self.tn_truoc_thue * 0.05

        elif self.tn_chiu_thue >= 5000000 and self.tn_chiu_thue < 10000000:
            self.thue_TNCN = self.tn_truoc_thue * 0.1 - 250000
        
        elif self.tn_chiu_thue >= 10000000 and self.tn_chiu_thue < 18000000:
            self.thue_TNCN = self.tn_truoc_thue * 0.15 - 750000
            
        elif self.tn_chiu_thue >= 18000000 and self.tn_chiu_thue < 32000000:
            self.thue_TNCN = self.tn_truoc_thue * 0.20 - 1650000

        elif self.tn_chiu_thue >= 32000000 and self.tn_chiu_thue < 52000000:
            self.thue_TNCN = self.tn_truoc_thue * 0.25 - 3250000
            
        elif self.tn_chiu_thue >= 52000000 and self.tn_chiu_thue < 80000000:
            self.thue_TNCN = self.tn_truoc_thue * 0.30 - 5850000
        
        else:
            self.thue_TNCN = self.tn_truoc_thue * 0.35 - 9850000

        self.tn_sau_thue = self.tn_truoc_thue - self.thue_TNCN
        
    def ket_qua(self):
        print(f'Thống kê của nhân viên: {self.ho_ten}')
        print(f'Thu nhập trước thuế: {self.tn_truoc_thue:,}')
        print(f'Thu nhập chịu thuế: {self.tn_chiu_thue:,}')
        print(f'Thuế thu nhập cá nhân: {self.thue_TNCN:,}')
        print(f'Thực lĩnh: {self.tn_sau_thue:,}')
        
    def __del__(self):
        print("Dtor NhanVien")
        pass
    
    def __str__(self):
        self.tinh_luong()
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

class QuanLyNhanVien:
    '''
    class QuanLyNhanVien
    '''
    def __init__(self):
        print('ctor QuanLyNhanVien')
        self.__danh_sach_NV = []

    def NhapNhanVien(self):
        while(1):
            chon = int(input("Chọn kiểu nhân viên: 1 Nhân viên sản xuất; 2 Nhân viên kinh doanh; 0 Hủy: "))              
            if not chon:
                break
            else:
                ho_ten = input("Nhập họ và tên nhân viên: ")
                he_so_luong = float(input("Nhập hệ số lương: "))
                giam_tru_gia_canh = int(input("Nhập số người giảm trừ gia cảnh: "))
                if chon == 1:
                    doanh_so = int(input("Nhập danh số cho nhân viên kinh doanh: "))
                    nv = NhanVienKinhDoanh(ho_ten, he_so_luong, giam_tru_gia_canh, doanh_so)
                elif chon == 2:
                    san_pham = int(input("Nhập số sản phẩm cho nhân viên sản xuất: "))
                    nv = NhanVienSanXuat(ho_ten, he_so_luong, giam_tru_gia_canh, san_pham)
                self.__danh_sach_NV.append(nv)

    def ThongTinNhanVien(self):
        print(f'Số nhân viên đang được quản lý: {len(self.__danh_sach_NV)}')
        for i in range(len(self.__danh_sach_NV)):
            print(self.__danh_sach_NV[i].loaiNhanVien())
            print(f'Nhân viên {i + 1}: {self.__danh_sach_NV[i]}')

    def __del__(slef):
        print('dtor QuanLyNhanVien')
        
    def __str__(self):
        for nv in self.__danh_sach_NV:
            print(nv)

class NhanVienKinhDoanh(NhanVien):
    def __init__(self, ho_ten, he_so_luong, gia_canh, ty_le_kinh_doanh):
        self.luong_cb = 1600000
        super().__init__(ho_ten, he_so_luong, gia_canh, ty_le_kinh_doanh * self.luong_cb)
    
    def loaiNhanVien(self):
        return 'Nhân viên kinh doanh'

class NhanVienSanXuat(NhanVien):
    def __init__(self, ho_ten, he_so_luong, gia_canh, so_san_pham):
        self.don_gia_gia_cong = 15000
        self.dinh_muc_san_pham = 450
        if so_san_pham > self.dinh_muc_san_pham:
            super().__init__(ho_ten, he_so_luong, gia_canh, (so_san_pham - self.dinh_muc_san_pham) * self.don_gia_gia_cong)

    def loaiNhanVien(self):
        return 'Nhân viên Sản xuất'


def main():
    # ho_ten = input("Nhập họ và tên nhân viên: ")
    # he_so_luong = int(input("Nhập hệ số lương: "))
    # giam_tru_gia_canh = int(input("Nhập số người giảm trừ gia cảnh: "))
    # thu_lao = int(input("Nhập thù lao công việc: "))
    
    # nv1 = NhanVien('Lại Minh Hà', 2.67, 1, 12000000)
    # nv1.tinh_luong()
    # nv1.ket_qua()
    # nv2 = NhanVien(ho_ten, he_so_luong, giam_tru_gia_canh, thu_lao)
    # print(nv2)
    mgr = QuanLyNhanVien()
    mgr.NhapNhanVien()
    mgr.ThongTinNhanVien()
    # mgr.__str__()
    # print(nv)
    
if __name__ == "__main__":
    main()
