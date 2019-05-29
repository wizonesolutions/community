from talon import app, tap, ctrl, actions


# from talon_plugins import speech
# from talon_plugins.speech import menu


def set_speech_on_start():
    # Disable speech recognition on startup.
    actions.speech.toggle(False)


app.register('launch', set_speech_on_start)

# menu.lang_activate(menu.active_langs['en_US'])


# # Swap RollerMouse polarity when holding shift
# class ShiftScroll:
#     def __init__(self):
#         tap.register(tap.KEY, self.on_key)
#         tap.register(tap.SCROLL, self.on_scroll)
#         self.shift_held = False
#         self.scroll_counter = 0
#
#     def on_key(self, e):
#         if e.key == 'shift':
#             self.shift_held = 'shift' in e.mods
#
#     def on_scroll(self, e):
#         if self.shift_held:
#             if self.scroll_counter > 0:
#                 self.scroll_counter -= 1
#                 print("STARTSKIP skipped, already horizontal")
#                 print(vars(e))
#                 print("ENDSKIP end skip")
#             else:
#                 print("STARTINVERT inverting scroll because shift held")
#                 print(vars(e))
#                 print("ENDINVERT")
#                 self.scroll_counter += 1
#                 e.block()
#                 ctrl.mouse_scroll(e.dy, e.dx, by_lines=e.by_line)
#
# ShiftScroll()
