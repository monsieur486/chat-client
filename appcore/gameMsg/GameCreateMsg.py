class GameCreateMsg:
    def __init__(self,
                 denomination,
                 private,
                 password,
                 maxPlayers,
                 isWithChat,
                 isWithRelance,
                 isWithAnnonce,
                 isWithRound,
                 isWithBelge,
                 isWithPetite,
                 isWithGarde,
                 isWithGardeSans,
                 user,
                 nickname
                 ):
        self.denomination = denomination
        self.private = private
        self.password = password
        self.maxPlayers = maxPlayers
        self.isWithChat = isWithChat
        self.isWithRelance = isWithRelance
        self.isWithAnnonce = isWithAnnonce
        self.isWithRound = isWithRound
        self.isWithBelge = isWithBelge
        self.isWithPetite = isWithPetite
        self.isWithGarde = isWithGarde
        self.isWithGardeSans = isWithGardeSans
        self.user = user
        self.nickname = nickname
