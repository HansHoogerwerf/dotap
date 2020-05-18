import win32api
import win32con
from ctypes import windll

left = 850
top = 330
clicks = 2500

pixels = [100, 300, 500, 700]


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def get_color_at_xy(x, y):
    dc = windll.user32.GetDC(0)
    rgb = windll.gdi32.GetPixel(dc, x, y)
    r = rgb & 0xff
    g = (rgb >> 8) & 0xff
    b = (rgb >> 16) & 0xff
    return r, g, b


if __name__ == '__main__':
    counter = 0
    while counter < clicks:
        for pixel_y in pixels:
            for pixel_x in pixels:
                color = get_color_at_xy(left + pixel_x, top + pixel_y)
                # print(left + pixel_x, top + pixel_y, color)
                if color[0] is 0:
                    click(left + pixel_x, top + pixel_y)
                    counter += 1
