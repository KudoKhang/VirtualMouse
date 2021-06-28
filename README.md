# Virtual Mouse

Với ứng dụng này chúng ta có thể điều khiển con trỏ máy tính bằng ngón tay thông qua camera. Chúng ta có thể mở rộng thêm các tác vụ tùy chọn trước ví dụ như 3 ngón thì chụp màn hình, 4 ngón thì chuyển slide thuyết trình... 

# How it work

- Chúng ta sử dụng [mediapipe](https://mediapipe.dev/) để nhận diện các landmarks trên bàn tay.

- Dựa vào các điểm landmarks đó để tính toán các positions cụ thể (điểm đầu ngón, ngón thứ nhất, ngón thứ 2)

- Sau khi có tọa độ điểm đầu ngón tay ta chuyển nó thành tọa độ của chuột bằng [autopy](https://pypi.org/project/autopy/) và thực hiện điều khiển

# Installations

Để khởi chạy được ứng dụng đầu tiên ta cần phải cài đặt các thư viện sau:

```
pip install cv2
pip install numpy
pip install mediapipe
pip install autopy
```

# Usage

Mở terminal và clone ứng dụng về sau đó khởi chạy:

```
git clone https://github.com/KudoKhang/VirtualMouse
cd VirtualMouse
python ControlMouse.py
```

# Extend

- Với tọa độ các điểm của ngón tay, thể gán thêm cho nó những tác vụ cần thiết trong trường hợp cụ thể
- Viết giao diện người dùng GUI cho dễ sử dụng
- Tối ưu thao tác của ngón tay sau cho việc điều khiển mượt mà hơn
