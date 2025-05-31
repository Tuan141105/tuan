từ selenium nhập webdriver
từ selenium.webdriver.common.by nhập khẩu Bởi
từ selenium.webdriver.chrome.service nhập Dịch vụ
từ selenium.webdriver.support.ui nhập WebDriverWait
từ selenium.webdriver.support nhập expected_conditions dưới dạng EC
thời gian nhập khẩu

# Cấu hình webdriver
trình điều khiển = webdriver.Chrome()

# Truy cập trang web có thanh tiến trình
trình điều khiển . lấy ( "https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html" )

start_button = driver.find_element(Theo.ID, "cricle-btn")
nút bắt đầu.nhấp()

chờ = WebDriverWait(trình điều khiển, 30)

thử:
    trong khi Đúng:
        progress_element = driver.find_element(Bởi.CLASS_NAME, "percenttext")
        phần trăm = progress_element.text
        print ( f"Tiến trình: { phần trăm } " )
        nếu phần trăm == "100%":
            in ( "Hoàn tất!" )
            phá vỡ
        thời gian . ngủ ( 0.5 )
ngoại trừ Ngoại lệ như e:
    print ( "Có lỗi xảy ra:" , e )

# Đóng trình duyệt
trình điều khiển . thoát ()