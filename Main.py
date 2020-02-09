"""
Eddies videos people playing pool by fast-forwarding through parts where the balls aren't moving
Conrad Stevens
25/01/2020
"""
import processingScripts.VideoData as RunVideo
import processingScripts.ProcessVido as ProcessVideo
import editingScripts.VideoEditor as VideoEdditor


if __name__ == '__main__':
    # Names and dirs
    input_video             = 'MaxEveryVid.mp4'
    process_output_video    = 'outputProcessVid.mp4'
    export_name             = 'OutputVid.mp4'

    # Nobs and Daile
    num_frames_analyzed     = 29
    percent_frames_cut_off  = 0.8
    movement_sensitivity    = 2
    min_ball_size           = 25
    max_ball_size           = 100

    # What To Draw
    draw_all_contours       = False
    draw_ball_contours      = True
    play_video_as_loading   = False

    # Engine
    video = RunVideo.VIDEO(input_video, process_output_video, min_ball_size,
                           max_ball_size, movement_sensitivity, draw_all_contours)

    #motherBoard = ProcessVideo.MOTHERBOARD(video, num_frames_analyzed, percent_frames_cut_off,
    #                                       draw_ball_contours, play_video_as_loading)

    #motherBoard.processVideo()
    videoEditor = VideoEdditor.VIDEOEDDITOR(input_video, export_name, video.fps)
    videoEditor.editVideo()


