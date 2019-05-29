# from talon import actions, cron, tap
#
# job = None
#
# def timeout():
#     global job
#     job = None
#     cron.after('0s', actions.speech.enable)
#
# def on_key(e):
#     global job
#     if e.keyboard_type != 198 and (job or actions.speech.enabled()):
#         cron.after('0s', actions.speech.disable)
#
#         if job:
#             cron.cancel(job)
#         job = cron.after('500ms', timeout)
#
# tap.register(tap.KEY, on_key)
