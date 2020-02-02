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
    process_output_video    = 'outputProcessVid'
    export_name             = 'outputProcessVid.mp4'

    # Nobs and Daile
    num_frames_analyzed     = 6
    percent_frames_cut_off  = 0.5
    movement_sensitivity    = 5
    min_ball_size           = 25
    max_ball_size           = 90

    # What To Draw
    draw_all_contours       = False
    draw_ball_contours      = True
    play_video_as_loading   = True

    # Engine
    video = RunVideo.VIDEO(input_video, process_output_video, min_ball_size,
                           max_ball_size, movement_sensitivity, draw_all_contours)

    # motherBoard = ProcessVideo.MOTHERBOARD(video, 5, 0.5, draw_ball_contours, play_video_as_loading)
    # motherBoard.processVideo()
    videoEditor = VideoEdditor.VIDEOEDDITOR('MaxEveryVid.mp4', export_name, 30)
    videoEditor.editVideo()


