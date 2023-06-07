#Skeleton Program code for the AQA A Level Paper 1 Summer 2023 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA Programmer Team
#developed in the Python 3.9 programming environment

import random

class Dastan:
    def __init__(self, R, C, NoOfPieces):
        self._Board = []
        self._Players = []
        self._MoveOptionOffer = []
        self.getUsernames()
        self.__CreateMoveOptions()
        self._NoOfRows = R
        self._NoOfColumns = C
        self._MoveOptionOfferPosition = 0
        self.__CreateMoveOptionOffer()
        while True:
            location1 = input("Player 1 enter mirza/kotla location:")
            if location1[0] == "1" and int(location1[1]) > 0 and int(location1[1]) < self._NoOfColumns:
                break
        while True:
            location2 = input("Player 2 enter mirza/kotla location:")
            if location2[0] == "6" and int(location2[1]) > 0 and int(location2[1]) < self._NoOfColumns:
                break
        self.__CreateBoard(location1,location2)
        self.__CreatePieces(NoOfPieces,location1,location2)
        self._CurrentPlayer = self._Players[0]

# wikibooks prediction 4
    def getUsernames(self):
        name1 = input("Player1 please enter name:")
        while True:
            name2 = input("Player2 please enter name:")
            if name1 != name2:
                break
        self._Players.append(Player(name1, 1))
        self._Players.append(Player(name2, -1))

    def __DisplayBoard(self):
        print("\n" + "   ", end="")
        for Column in range(1, self._NoOfColumns + 1):
            print(str(Column) + "  ", end="")
        print("\n" + "  ", end="")
        for Count in range(1, self._NoOfColumns + 1):
            print("---", end="")
        print("-")
        for Row in range(1, self._NoOfRows + 1):
            print(str(Row) + " ", end="")
            for Column in range(1, self._NoOfColumns + 1):
                Index = self.__GetIndexOfSquare(Row * 10 + Column)
                print("|" + self._Board[Index].GetSymbol(), end="")
                PieceInSquare = self._Board[Index].GetPieceInSquare()
                if PieceInSquare is None:
                    print(" ", end="")
                else:
                    print(PieceInSquare.GetSymbol(), end="")
            print("|")
        print("  -", end="")
        for Column in range(1, self._NoOfColumns + 1):
            print("---", end="")
        print()
        print()

    def __DisplayState(self):
        self.__DisplayBoard()
        print("Move option offer: " + self._MoveOptionOffer[self._MoveOptionOfferPosition])
        print()
        print(self._CurrentPlayer.GetPlayerStateAsString())
        print("Turn: " + self._CurrentPlayer.GetName())
        print()

    def __GetIndexOfSquare(self, SquareReference):
        Row = SquareReference // 10
        Col = SquareReference % 10
        return (Row - 1) * self._NoOfColumns + (Col - 1)

    def __CheckSquareInBounds(self, SquareReference):
        Row = SquareReference // 10
        Col = SquareReference % 10
        if Row < 1 or Row > self._NoOfRows:
            return False
        elif Col < 1 or Col > self._NoOfColumns:
            return False
        else:
            return True

    def __CheckSquareIsValid(self, SquareReference, StartSquare):
        if not self.__CheckSquareInBounds(SquareReference):
            return False
        PieceInSquare = self._Board[self.__GetIndexOfSquare(SquareReference)].GetPieceInSquare()
        if PieceInSquare is None:
            if StartSquare:
                return False
            else:
                return True
        elif self._CurrentPlayer.SameAs(PieceInSquare.GetBelongsTo()):
            if StartSquare:
                return True
            else:
                return False
        else:
            if StartSquare:
                return False
            else:
                return True

    def __CheckIfGameOver(self):
        Player1HasMirza = False
        Player2HasMirza = False
        for S in self._Board:
            PieceInSquare = S.GetPieceInSquare()
            if PieceInSquare is not None:
                if S.ContainsKotla() and PieceInSquare.GetTypeOfPiece() == "mirza" and not PieceInSquare.GetBelongsTo().SameAs(S.GetBelongsTo()):
                    return True
                elif PieceInSquare.GetTypeOfPiece() == "mirza" and PieceInSquare.GetBelongsTo().SameAs(self._Players[0]):
                    Player1HasMirza = True
                elif PieceInSquare.GetTypeOfPiece() == "mirza" and PieceInSquare.GetBelongsTo().SameAs(self._Players[1]):
                    Player2HasMirza = True
        return not (Player1HasMirza and Player2HasMirza)

    def __GetSquareReference(self, Description):
        SelectedSquare = int(input("Enter the square " + Description + " (row number followed by column number): "))
        return SelectedSquare

    def __UseMoveOptionOffer(self):
        ReplaceChoice = int(self.__ValidateUserInput(("Choose the move option from your queue to replace (1 to 5): "+))
        self._CurrentPlayer.UpdateMoveOptionQueueWithOffer(ReplaceChoice - 1, self.__CreateMoveOption(self._MoveOptionOffer[self._MoveOptionOfferPosition], self._CurrentPlayer.GetDirection()))
        self._CurrentPlayer.ChangeScore(-(10 - (ReplaceChoice * 2)))
        self._MoveOptionOfferPosition = random.randint(0, 4)

    def __GetPointsForOccupancyByPlayer(self, CurrentPlayer):
        ScoreAdjustment = 0
        for S in self._Board:
            ScoreAdjustment += (S.GetPointsForOccupancy(CurrentPlayer))
        return ScoreAdjustment

    def __UpdatePlayerScore(self, PointsForPieceCapture):
        self._CurrentPlayer.ChangeScore(self.__GetPointsForOccupancyByPlayer(self._CurrentPlayer) + PointsForPieceCapture)

    def __CalculatePieceCapturePoints(self, FinishSquareReference):
        if self._Board[self.__GetIndexOfSquare(FinishSquareReference)].GetPieceInSquare() is not None:
            return self._Board[self.__GetIndexOfSquare(FinishSquareReference)].GetPieceInSquare().GetPointsIfCaptured()
        return 0

    def __ValidateUserInput(PromptString):
        while True:
            inputFromUser = input(PromptString)
            try:
                int(inputFromUser)
            except ValueError():
                print("ERROR - must provide an interger, try again")
            else:
                break
        return inputFromUser

    def PlayGame(self):
        GameOver = False
        while not GameOver:
            self.__DisplayState()
            SquareIsValid = False
            Choice = 0
            while Choice < 1 or Choice > 3 and Choice != 10:
                if self._CurrentPlayer.GetSpaceJumpUsed() is not True:
                    print("10 to use the space jump or")
                Choice = int(self.__ValidateUserInput("Choose move option to use from queue (1 to 3) or 9 to take the offer: "))
                if Choice == 9:
                    self.__UseMoveOptionOffer()
                    self.__DisplayState()
                    # wikibooks prediction - change turn after moveoption offer is taken
                    # this can be done with a break 
                    break
                elif Choice == 10:
                    self._CurrentPlayer.SetSpaceJumpUsed()
                    while True:
                        StartSquareReference = self.__GetSquareReference("containing the piece to space jump:")
                        if self.__CheckSquareIsValid(StartSquareReference, True):
                            break
                        print("Invalid start square, retry")
                    while True:
                        FinishSquareReference = int(str(random.randint(1,6)) + str(random.randint(1,6)))
                        if self._Board[self.__GetIndexOfSquare(FinishSquareReference)].GetPieceInSquare() is not None:
                            if self._Board[self.__GetIndexOfSquare(FinishSquareReference)].GetPieceInSquare().GetBelongsTo().SameAs(self._CurrentPlayer) is not True:
                                break
                        elif self._Board[self.__GetIndexOfSquare(FinishSquareReference)].GetPieceInSquare() is None:
                            break
                    PointsForPieceCapture = self.__CalculatePieceCapturePoints(FinishSquareReference)
                    self.__UpdateBoard(StartSquareReference, FinishSquareReference)
                    self.__UpdatePlayerScore(PointsForPieceCapture)
                    print("New score: " + str(self._CurrentPlayer.GetScore()) + "\n")
            
            if Choice != 10 and Choice != 9:
                while not SquareIsValid:
                    StartSquareReference = self.__GetSquareReference("containing the piece to move")
                    SquareIsValid = self.__CheckSquareIsValid(StartSquareReference, True)
                SquareIsValid = False
                self.__showMoves(Choice, StartSquareReference)
                # wikibooks prediction 2
                if self._CurrentPlayer._Queue.GetMoveOptionInPosition(Choice-1).GetName() == "rook":
                    FinishRow = int(str(StartSquareReference)[0])
                    column = int(str(StartSquareReference)[1])
                    while FinishRow <= self._NoOfRows and FinishRow > 0:
                        # iterate the current row location depending on the current player direction
                        FinishRow += self._CurrentPlayer.GetDirection()
                        if FinishRow < 1:
                            FinishRow -= self._CurrentPlayer.GetDirection()
                            FinishSquareReference = int(str(FinishRow)+str(column))
                            break
                        elif FinishRow > self._NoOfRows:
                            FinishRow -= self._CurrentPlayer.GetDirection()
                            FinishSquareReference = int(str(FinishRow)+str(column))
                            break
                        # check if the new position is ocupied by a piece
                        elif self._Board[self.__GetIndexOfSquare(int(str(FinishRow)+str(column)))].GetPieceInSquare() is not None:
                            # if so set this as finishsquare
                            FinishSquareReference = int(str(FinishRow)+str(column))
                            break
                while not SquareIsValid and (self._CurrentPlayer._Queue.GetMoveOptionInPosition(Choice-1).GetName() != "rook"):
                    # wikibooks predictions 3
                    while True:
                        FinishSquareReference = self.__GetSquareReference("to move to")
                        SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)
                        if self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, FinishSquareReference) is True and SquareIsValid:
                            break
                        print("Invalid end square - please re-enter")
                MoveLegal = self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, FinishSquareReference)
                if self._CurrentPlayer._Queue.GetMoveOptionInPosition(Choice-1).GetName() == "rook":
                    MoveLegal = True
                if MoveLegal :
                    PointsForPieceCapture = self.__CalculatePieceCapturePoints(FinishSquareReference)
                    self._CurrentPlayer.ChangeScore(-(Choice + (2 * (Choice - 1))))
                    self._CurrentPlayer.UpdateQueueAfterMove(Choice)
                    self.__UpdateBoard(StartSquareReference, FinishSquareReference)
                    self.__UpdatePlayerScore(PointsForPieceCapture)
                    print("New score: " + str(self._CurrentPlayer.GetScore()) + "\n")
                if self._CurrentPlayer.SameAs(self._Players[0]):
                    self._CurrentPlayer = self._Players[1]
                else:
                    self._CurrentPlayer = self._Players[0]
                GameOver = self.__CheckIfGameOver()
            elif self._CurrentPlayer.SameAs(self._Players[0]):
                self._CurrentPlayer = self._Players[1]
            else:
                self._CurrentPlayer = self._Players[0]
            GameOver = self.__CheckIfGameOver()
        self.__DisplayState()
        self.__DisplayFinalResult()

    # wikibooks prediction - show possible moves of a piece selected
    def __showMoves(self, Choice, StartSquareReference):
        # showing the possible moves on a board after the user selects the starting square could be done by adding symbols to the board
        # make copy of code to display the board.
        # however check if the square being currently displayed is valid using using CheckIfThereIsAMoveToSquare() boolean return value
        moveoption = self._CurrentPlayer._Queue.GetMoveOptionInPosition(Choice-1)
        print("\n" + "   ", end="")
        for Column in range(1, self._NoOfColumns + 1):
            print(str(Column) + "  ", end="")
        print("\n" + "  ", end="")
        for Count in range(1, self._NoOfColumns + 1):
            print("---", end="")
        print("-")
        for Row in range(1, self._NoOfRows + 1):
            print(str(Row) + " ", end="")
            for Column in range(1, self._NoOfColumns + 1):
                Index = self.__GetIndexOfSquare(Row * 10 + Column)
                print("|" + self._Board[Index].GetSymbol(), end="")
                PieceInSquare = self._Board[Index].GetPieceInSquare()
                if moveoption.CheckIfThereIsAMoveToSquare(StartSquareReference, int(str(Row)+str(Column))):
                    print("^", end="")
                elif PieceInSquare is None:
                    print(" ", end="")
                else:
                    print(PieceInSquare.GetSymbol(), end="")
            print("|")
        print("  -", end="")
        for Column in range(1, self._NoOfColumns + 1):
            print("---", end="")
        print()
        print()

    def __UpdateBoard(self, StartSquareReference, FinishSquareReference):
        self._Board[self.__GetIndexOfSquare(FinishSquareReference)].SetPiece(self._Board[self.__GetIndexOfSquare(StartSquareReference)].RemovePiece())

    def __DisplayFinalResult(self):
        if self._Players[0].GetScore() == self._Players[1].GetScore():
            print("Draw!")
        elif self._Players[0].GetScore() > self._Players[1].GetScore():
            print(self._Players[0].GetName() + " is the winner!")
        else:
            print(self._Players[1].GetName() + " is the winner!")

    def __CreateBoard(self, loc1, loc2):
        for Row in range(1, self._NoOfRows + 1):
            for Column in range(1, self._NoOfColumns + 1):
                if Row == 1 and Column == int(loc1[1]):
                    S = Kotla(self._Players[0], "K")
                elif Row == self._NoOfRows and Column == int(loc2[1]):
                    S = Kotla(self._Players[1], "k")
                else:
                    S = Square()
                self._Board.append(S)

    def __CreatePieces(self, NoOfPieces,loc1,loc2):
        for Count in range(1, NoOfPieces + 1):
            CurrentPiece = Piece("piece", self._Players[0], 1, "!")
            self._Board[self.__GetIndexOfSquare(2 * 10 + Count + 1)].SetPiece(CurrentPiece)
        CurrentPiece = Piece("mirza", self._Players[0], 5, "1")
        self._Board[self.__GetIndexOfSquare(int(loc1))].SetPiece(CurrentPiece)
        for Count in range(1, NoOfPieces + 1):
            CurrentPiece = Piece("piece", self._Players[1], 1, '"')
            self._Board[self.__GetIndexOfSquare((self._NoOfRows - 1) * 10 + Count + 1)].SetPiece(CurrentPiece)
        CurrentPiece = Piece("mirza", self._Players[1], 5, "2")
        self._Board[self.__GetIndexOfSquare(int(loc2))].SetPiece(CurrentPiece)

    def __CreateMoveOptionOffer(self):
        self._MoveOptionOffer.append("jazair")
        self._MoveOptionOffer.append("chowkidar")
        self._MoveOptionOffer.append("cuirassier")
        self._MoveOptionOffer.append("ryott")
        self._MoveOptionOffer.append("faujdar")
        self._MoveOptionOffer.append("tibblecross")
        self._MoveOptionOffer.append("rook")

    # wikibooks prediction 1
    def __CreateTibbleCrossMoveOption(self, Direction):
        NewMoveOption = MoveOption("tibblecross")
        NewMove = Move(2,2)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-2,2)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-2,-2)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(2,-2)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption 

    # wikibooks prediction 2
    def __CreateRookMoveOption(self, Direction):
        NewMoveOption = MoveOption("rook")
        NewMove = Move(0,0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateRyottMoveOption(self, Direction):
        NewMoveOption = MoveOption("ryott")
        NewMove = Move(0, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(1 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateFaujdarMoveOption(self, Direction):
        NewMoveOption = MoveOption("faujdar")
        NewMove = Move(0, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateJazairMoveOption(self, Direction):
        NewMoveOption = MoveOption("jazair")
        NewMove = Move(2 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(2 * Direction, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(2 * Direction, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateCuirassierMoveOption(self, Direction):
        NewMoveOption = MoveOption("cuirassier")
        NewMove = Move(1 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(2 * Direction, 0)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(1 * Direction, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(1 * Direction, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateChowkidarMoveOption(self, Direction):
        NewMoveOption = MoveOption("chowkidar")
        NewMove = Move(1 * Direction, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(1 * Direction, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, 1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(-1 * Direction, -1 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, 2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        NewMove = Move(0, -2 * Direction)
        NewMoveOption.AddToPossibleMoves(NewMove)
        return NewMoveOption

    def __CreateMoveOption(self, Name, Direction):
        if Name == "chowkidar":
            return self.__CreateChowkidarMoveOption(Direction)
        elif Name == "ryott":
            return self.__CreateRyottMoveOption(Direction)
        elif Name == "tibblecross":
            return self.__CreateTibbleCrossMoveOption(Direction)
        elif Name == "faujdar":
            return self.__CreateFaujdarMoveOption(Direction)
        elif Name == "jazair":
            return self.__CreateJazairMoveOption(Direction)
        elif Name == "rook":
            return self.__CreateRookMoveOption(Direction)
        else:
            return self.__CreateCuirassierMoveOption(Direction)

    def __CreateMoveOptions(self):
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("tibblecross", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("rook", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("ryott", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("chowkidar", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("cuirassier", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("faujdar", 1))
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("jazair", 1))
        self._Players[0].shuffleMoveOptionQ()
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("tibblecross", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("rook", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("ryott", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("chowkidar", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("jazair", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("faujdar", -1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("cuirassier", -1))
        self._Players[1].shuffleMoveOptionQ()

class Piece:
    def __init__(self, T, B, P, S):
        self._TypeOfPiece = T
        self._BelongsTo = B
        self._PointsIfCaptured = P
        self._Symbol = S

    def GetSymbol(self):
        return self._Symbol

    def GetTypeOfPiece(self):
        return self._TypeOfPiece

    def GetBelongsTo(self):
        return self._BelongsTo

    def GetPointsIfCaptured(self):
        return self._PointsIfCaptured

class Square:
    def __init__(self):
        self._PieceInSquare = None
        self._BelongsTo = None
        self._Symbol = " "

    def SetPiece(self, P):
        self._PieceInSquare = P

    def RemovePiece(self):
        PieceToReturn = self._PieceInSquare
        self._PieceInSquare = None
        return PieceToReturn

    def GetPieceInSquare(self):
        return self._PieceInSquare

    def GetSymbol(self):
        return self._Symbol

    def GetPointsForOccupancy(self, CurrentPlayer):
        return 0

    def GetBelongsTo(self):
        return self._BelongsTo

    def ContainsKotla(self):
        if self._Symbol == "K" or self._Symbol == "k":
            return True
        else:
            return False

class Kotla(Square):
    def __init__(self, P, S):
        super(Kotla, self).__init__()
        self._BelongsTo = P
        self._Symbol = S

    def GetPointsForOccupancy(self, CurrentPlayer):
        if self._PieceInSquare is None:
            return 0
        elif self._BelongsTo.SameAs(CurrentPlayer):
            if CurrentPlayer.SameAs(self._PieceInSquare.GetBelongsTo()) and (self._PieceInSquare.GetTypeOfPiece() == "piece" or self._PieceInSquare.GetTypeOfPiece() == "mirza"):
                return 5
            else:
                return 0
        else:
            if CurrentPlayer.SameAs(self._PieceInSquare.GetBelongsTo()) and (self._PieceInSquare.GetTypeOfPiece() == "piece" or self._PieceInSquare.GetTypeOfPiece() == "mirza"):
                return 1
            else:
                return 0

class MoveOption:
    def __init__(self, N):
        self._Name = N
        self._PossibleMoves = []

    def AddToPossibleMoves(self, M):
        self._PossibleMoves.append(M)

    def GetName(self):
        return self._Name

    def CheckIfThereIsAMoveToSquare(self, StartSquareReference, FinishSquareReference):
        StartRow = StartSquareReference // 10
        StartColumn = StartSquareReference % 10
        FinishRow = FinishSquareReference // 10
        FinishColumn = FinishSquareReference % 10
        for M in self._PossibleMoves:
            if StartRow + M.GetRowChange() == FinishRow and StartColumn + M.GetColumnChange() == FinishColumn:
                return True
        return False

class Move:
    def __init__(self, R, C):
        self._RowChange = R
        self._ColumnChange = C

    def GetRowChange(self):
        return self._RowChange

    def GetColumnChange(self):
        return self._ColumnChange

class MoveOptionQueue:
    def __init__(self):
        self.__Queue = []

    def GetQueueAsString(self):
        QueueAsString = ""
        Count = 1
        for M in self.__Queue:
            QueueAsString += str(Count) + ". " + M.GetName() + "   "
            Count += 1
        return QueueAsString

    def Add(self, NewMoveOption):
        self.__Queue.append(NewMoveOption)

    def Replace(self, Position, NewMoveOption):
        self.__Queue[Position] = NewMoveOption

    def MoveItemToBack(self, Position):
        Temp = self.__Queue[Position]
        self.__Queue.pop(Position)
        self.__Queue.append(Temp)

    def GetMoveOptionInPosition(self, Pos):
        return self.__Queue[Pos]
    
    def shuffle(self):
        random.shuffle(self.__Queue)

class Player:
    def __init__(self, N, D):
        self.__Score = 100
        self.__Name = N
        self.__Direction = D
        self._Queue = MoveOptionQueue()
        self._SpaceJumpUsed = False

    def shuffleMoveOptionQ(self):
        self._Queue.shuffle()

    # wikibooks prediction 4 - spacejump 
    def GetSpaceJumpUsed(self):
        return self._SpaceJumpUsed

    def SetSpaceJumpUsed(self):
        self._SpaceJumpUsed = True

    def SameAs(self, APlayer):
        if APlayer is None:
            return False
        elif APlayer.GetName() == self.__Name:
            return True
        else:
            return False

    def GetPlayerStateAsString(self):
        return self.__Name + "\n" + "Score: " + str(self.__Score) + "\n" + "Move option queue: " + self._Queue.GetQueueAsString() + "\n"

    def AddToMoveOptionQueue(self, NewMoveOption):
        self._Queue.Add(NewMoveOption)

    def UpdateQueueAfterMove(self, Position):
        self._Queue.MoveItemToBack(Position - 1)

    def UpdateMoveOptionQueueWithOffer(self, Position, NewMoveOption):
        self._Queue.Replace(Position, NewMoveOption)

    def GetScore(self):
        return self.__Score

    def GetName(self):
        return self.__Name

    def GetDirection(self):
        return self.__Direction

    def ChangeScore(self, Amount):
        self.__Score += Amount

    def CheckPlayerMove(self, Pos, StartSquareReference, FinishSquareReference):
        Temp = self._Queue.GetMoveOptionInPosition(Pos - 1)
        return Temp.CheckIfThereIsAMoveToSquare(StartSquareReference, FinishSquareReference)

def Main():
    ThisGame = Dastan(6, 6, 4)
    ThisGame.PlayGame()
    print("Goodbye!")
    input()

if __name__ == "__main__":
    Main()
