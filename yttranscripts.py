from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
def youtube_cap(input_txt):
    # for i in vid_id:
        
    vid_id=input_txt
    #https://www.youtube.com/watch?v=sAzL4XMke80
# https://www.youtube.com/watch?v=MD2HdHylzxo
    data =yta.get_transcript(vid_id)
    transcript=''
    for value in data:
        for key,val in value.items():
            if key=='text':
                transcript+=" " +val
    l=transcript.splitlines()
    final_tra=" ".join(l)
    #print(final_tra)
    return final_tra



#file=open("Transcripts.txt","w")
#file.write(final_tra)