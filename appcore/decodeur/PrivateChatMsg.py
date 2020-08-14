# -*- coding: utf-8 -*-


from appcore.decodeur.ChatMsg import ChatMsg


class PrivateChatMsg(ChatMsg):
    def __init__(self, recipient, user, nickname, msgToSend):
        super().__init__(user, nickname, msgToSend)
        self.recipient = recipient
