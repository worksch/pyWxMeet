from pywinauto.application import Application
from win32gui import FindWindow

handle = FindWindow('TXGuiFoundation', '成员')
print('%x' % handle)

if handle == 0:
    print('腾讯会议没有打开成员窗口')
    exit()


app = Application(backend='uia').connect(handle=handle)
#app = Application().connect(title_re="成员", class_name="TXGuiFoundation")
#print(app.windows())
#print(app['腾讯会议'])
#print(app['InMeetingWnd'])
#app['InMeetingWnd']['memberListWnd'].print_control_identifiers()

# 成员列表
memberlist = app['InMeetingWnd']['memberListWnd']
#memberlist.print_control_identifiers()

memberyFrame = memberlist.ClientArea.memberViewFramePane
content_panel = memberyFrame.contentPanel
content_panel = content_panel.innerMemberPanel.inMeetingMemberViewFrame.contentPanel
#content_panel.memberListView.content_view.print_control_identifiers()
content_view = content_panel.memberListView.content_view
content_view.proxy_content_viewPane.print_control_identifiers(filename='C:/Users/weisf/Desktop/Test.txt')