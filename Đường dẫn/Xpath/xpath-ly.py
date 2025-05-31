
từ selenium nhập webdriver
từ selenium.webdriver.common.by nhập khẩu Bởi

trình điều khiển = webdriver.Chrome()
trình điều khiển . lấy ( "https://cellphones.com.vn" )

# Tìm kiếm theo XPath
phần tử = driver.find_element(By.XPATH, '//*[@id="box-content"]/div[2]/a')
in(phần tử.văn bản)