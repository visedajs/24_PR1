import tkinter as tk
from tkinter import messagebox
import random
import math
import time

# Avoti:
# * https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
# (Kā pievienot dziļumu jau eksistejošā alfa-beta algoritmam)
# (Struktura alfa-beta ar dziļumu ir lidziga strukturai alfa-beta ar pilno koku)
# * https://www.javatpoint.com/ai-alpha-beta-pruning
# * Jau esošais kodā minimax algoritms
# (Tiek modērņīzēts minimax algiritms,lai izveidotu alfa-beta)
# * Chat GPT conversation: https://chat.openai.com/share/6cb39c7c-b5ad-41a7-b127-e770643927da
def alphaBetaWithDepth(node, maximizingPlayer, depth, maxDepth, alpha, beta):
    global nodeCounter
    nodeCounter += 1

    gameOver = checkIfGameIsOver(node[1])
    
    # Principa var iztikt ari bez try catch, bet gadijumam ja gameOver varetu atgriezt kadu kļudu varetu atstat
    try:
        gameOver = checkIfGameIsOver(node[1])
    except Exception as e:
        gameOver = False
        print(f"Error when checking method checkIfGameIsOver: {e}")
    
    if gameOver:
        if depth == maxDepth:
            return returnBottomNodeHeureticValues(node[1])
        else:
            return returnBottomNodeHeureticValues(node[1])
    
    if maximizingPlayer:
        maxPoints = -math.inf
        best_node = None
        for i in node[1].children:
            points, _ = alphaBetaWithDepth([node[0], i[0]], not maximizingPlayer, depth+1, maxDepth, alpha, beta)
            if points > maxPoints:
                maxPoints = points
                best_node = i[0]
            alpha = max(alpha, points)
            if beta <= alpha:
                break  # Alfa beta nogrieziens
        return maxPoints, best_node
    else:
        minPoints = math.inf
        best_node = None
        for i in node[1].children:
            points, _ = alphaBetaWithDepth([node[0], i[0]], not maximizingPlayer, depth+1, maxDepth, alpha, beta)
            if points < minPoints:
                minPoints = points
                best_node = i[0]
            beta = min(beta, points)
            if beta <= alpha:
                break  # Alfa beta nogrieziens
        return minPoints, best_node

nodeCounter = 0


# Avoti:
# * https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/ 
# (Alfa-Beta struktura, kā notiek alfa-beta nogrieziens, kā izskatas alfa-beta algoritma struktura)
# * https://www.javatpoint.com/ai-alpha-beta-pruning
# (pseidokods, struktura)
# * Jau esošais kodā minimax algoritms
# (Tiek modērņīzēts minimax algiritms,lai izveidotu alfa-beta)
# * Chat GPT conersation: https://chat.openai.com/share/6cb39c7c-b5ad-41a7-b127-e770643927da
def alphaBeta(node, maximizingPlayer, alpha, beta):
    global nodeCounter
    global elapsed_time
    global time_list
    try:
        gameOver = checkIfGameIsOver(node[1])
    except:
        gameOver = False
    nodeCounter += 1

    if gameOver:
        return returnBottomNodeHeureticValues(node[1])
    
    if maximizingPlayer:
        maxPoints = -math.inf
        best_node = None
        for i in node[1].children:
            points = alphaBeta([node[0],i[0]], not maximizingPlayer, alpha, beta)
            if points[0] > maxPoints:
                maxPoints = points[0]
                best_node = i[0]
            alpha = max(alpha, points[0])
            if beta <= alpha:
                break  # Beta Pruning
        return [maxPoints, best_node]
    else:
        minPoints = math.inf
        best_node = None
        for i in node[1].children:
            points = alphaBeta([node[0],i[0]], not maximizingPlayer, alpha, beta)
            if points[0] < minPoints:
                minPoints = points[0]
                best_node = i[0]
            beta = min(beta, points[0])
            if beta <= alpha:
                break  # Alpha Pruning
        return [minPoints, best_node]

nodeCounter = 0


def returnBottomNodeHeureticValues(node):
    
    points = 0
    if node.total_points % 2 == 0:
        points = node.total_points - node.game_bank
    else:
        points = node.total_points + node.game_bank
    if points % 2 == 0:
        return [1, node] # player 1 wins
    else:
        return [-1, node] # player 2 wins
    
def checkIfGameIsOver(node):
    if node.value % 3 != 0 and node.value % 4 != 0 and node.value % 5 != 0:
        return True
    
    
def minimaxWithDepth(node, maximizingPlayer, depth, maxDepth):
    global nodeCounter
    try:
        gameOver = checkIfGameIsOver(node[1])
    except:
        gameOver = False
    nodeCounter = nodeCounter+1
    

    if gameOver or depth == maxDepth:
        return returnBottomNodeHeureticValues(node[1])
    
    if maximizingPlayer:
        maxPoints = -math.inf
        for i in node[1].children:
            points = minimaxWithDepth([node[0],i[0]], not maximizingPlayer, depth+1, maxDepth)
            if points[0] > maxPoints:
                maxPoints = points[0]
                best_node = i[0]

        return [maxPoints, best_node]
    else:
        minPoints = math.inf
        for i in node[1].children:
            points = minimaxWithDepth([node[0],i[0]], not maximizingPlayer, depth+1, maxDepth)
            if points[0] < minPoints:
                minPoints = points[0]
                best_node = i[0]
        return [minPoints, best_node]

nodeCounter = 0
# Izmantotie materiāli MiniMax algoritma izveidei:
# https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/
# https://www.youtube.com/watch?v=3nzupVMpZeA
# https://www.youtube.com/watch?v=Bk9hlNZc6sE
# https://www.youtube.com/watch?v=KU9Ch59-4vw
def minimax(node, maximizingPlayer):
    global nodeCounter
    

    try:
        gameOver = checkIfGameIsOver(node[1])
    except:
        gameOver = False
    nodeCounter = nodeCounter+1
    if gameOver:
        return returnBottomNodeHeureticValues(node[1])
    
    if maximizingPlayer:
        maxPoints = -math.inf
        for i in node[1].children:
            points = minimax([node[0],i[0]], not maximizingPlayer)
            if points[0] > maxPoints:
                maxPoints = points[0]
                best_node = i[0]

        return [maxPoints, best_node]
    else:
        minPoints = math.inf
        for i in node[1].children:
            points = minimax([node[0],i[0]], not maximizingPlayer)
            if points[0] < minPoints:
                minPoints = points[0]
                best_node = i[0]
        return [minPoints, best_node]

i = 0
def determineWinner(points, isHumanFirst):
    if isHumanFirst:
        if points == 1:
            print('Human')
            return "Human"
        else:
            print('Computer')
            return "Computer"
    else:
        if points == 1:
            print('Computer')
            return "Computer"
        else:
            print('Human')
            return "Human"


answer = ""
maxI = 0
elapsed_time = 0
time_list = []
def makeMove(treeStruct, bool, isHumanFirst):
    global answer
    global i
    global maxI
    global elapsed_time
    global time_list
    i = i+1
    maxI = maxI+1
    if bool: # if the player wants to get a negative number
        # print(treeStruct[0])
        if isHumanFirst:
            start_time = time.perf_counter_ns()
            node = minimax(treeStruct, not bool)
            end_time = time.perf_counter_ns()
            gameTime = (end_time - start_time)/ 1_000_000
            time_list.append(gameTime)
            # print(gameTime)
            elapsed_time = elapsed_time+gameTime
            answer = str(node[1].value)
        else:
            start_time = time.perf_counter_ns()
            # time.sleep(0.1)
            node = minimax(treeStruct, bool)
            end_time = time.perf_counter_ns()
            gameTime = (end_time - start_time)/ 1_000_000
            time_list.append(gameTime)
            # print(gameTime)
            elapsed_time = elapsed_time+gameTime
            answer = str(node[1].value)

        # print("Computer chose:" + str(node[1].value))
        if node[1].value % 3 == 0 or node[1].value % 4 == 0 or node[1].value % 5 == 0:
            makeMove([node[0],node[1]], not bool, isHumanFirst)
        

    return answer

def makeMoveDepth(treeStruct, bool, isHumanFirst, maxDepth):
    global answer
    global i
    global maxI
    global elapsed_time
    global time_list
    i = i+1
    maxI = maxI+1
    depth = 0
    if bool: # if the player wants to get a negative number
        print(treeStruct[0])
        if isHumanFirst:
            node = minimaxWithDepth(treeStruct, not bool, depth, maxDepth)
            end_time = time.perf_counter_ns()
            gameTime = (end_time - start_time)/ 1_000_000
            time_list.append(gameTime)
            # print(gameTime)
            elapsed_time = elapsed_time+gameTime
            answer = str(node[1].value)
        else:
            start_time = time.perf_counter_ns()
            node = minimaxWithDepth(treeStruct, bool, depth, maxDepth)
            end_time = time.perf_counter_ns()
            gameTime = (end_time - start_time)/ 1_000_000
            time_list.append(gameTime)
            # print(gameTime)
            elapsed_time = elapsed_time+gameTime
            answer = str(node[1].value)
        # print("Computer chose:" + str(node[1].value))
        maxDepth = maxDepth+2
        if node[1].value % 3 == 0 or node[1].value % 4 == 0 or node[1].value % 5 == 0:
            makeMoveDepth([node[0],node[1]], not bool, isHumanFirst, maxDepth)
   
    return answer


# Izmantotie materiāli koka struktūras izveidei:
# https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
class Tree:
    def __init__(self, value, total_points, game_bank, depth):
        self.value = value # panem value no Tree
        self.total_points = total_points
        self.game_bank = game_bank
        self.children = [] # uztaisa tuksu list prieks children
        depth = depth+1
        self.add_child(value, total_points, game_bank, depth) #izsauc funkciju add_child un iedod value, no kura meginas dalit ar 3, 4, 5

    def add_child(self, parent,total_points, game_bank, depth):
        for i in range(3,6): # loopo par i padarot 3,4,5
            if parent % i == 0:
                child_value = parent//i
                if child_value % 2 == 0:
                    if child_value % 5 == 0:
                        child = Tree(child_value, total_points+1, game_bank+1, depth)
                        self.children.append([child, i, total_points+1, game_bank+1, depth])
                    else:
                        child = Tree(child_value, total_points+1, game_bank, depth)
                        self.children.append([child, i, total_points+1, game_bank, depth])
                else:
                    if child_value % 5 == 0:
                        child = Tree(child_value, total_points-1, game_bank+1, depth)
                        self.children.append([child, i, total_points-1, game_bank+1, depth])
                    else:
                        child = Tree(child_value, total_points-1, game_bank, depth)
                        self.children.append([child, i, total_points-1, game_bank, depth])

    # calculates and shows the points for the game which determines, if the player who started the game wins or not
    def calcWinningPoints(self, total_points, game_bank):
        if total_points % 2 == 0:
            points = total_points - game_bank
        else:
            points = total_points + game_bank

        return points

    # Chat GPT jautāts jautājums: Kā var izvadīt koku, lai redzētu, kā viņš izskatās konsolē, kā arī, lai redzētu, kāds ir beigu punktu skaits
    def print_tree(self, indent="", last=True, depth=0):
        print(indent, '|__' if last else '|--', self.value, "=> ", self.calcWinningPoints(self.total_points, self.game_bank), sep='')
        indent += '   ' if last else '|  '
        if not self.children:
            global skibidi_toilet
            skibidi_toilet = depth
        for i, child in enumerate(self.children):
            last = i == len(self.children) - 1
            child[0].print_tree(indent, last, depth + 1)
            
    # Koks bez papildu vērtībām pie virsotnēm
    # def print_tree(self, indent="", last=True, depth=0):
    #     print(indent, '|__' if last else '|--', self.value, sep='')
    #     indent += '   ' if last else '|  '
    #     if not self.children:
    #         global skibidi_toilet
    #         skibidi_toilet = depth
    #     for i, child in enumerate(self.children):
    #         last = i == len(self.children) - 1
    #         child[0].print_tree(indent, last, depth + 1)


class GraphicalUserInterface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Inicializē cilvēka uzvaru skaitus
        self.humanRoundsWon = 0
        self.computerRoundsWon = 0

        # loga izveidošana
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.screenWidth = int(screen_width * 0.5)
        self.screenHeight = int(screen_height * 0.5)
        
        self.geometry(str(self.screenWidth) + "x" + str(self.screenHeight))
        self.title("Komanda 24 1PD")

        self.currentScreen = None
        self.showMainScreen()
        
        self.protocol("WM_DELETE_WINDOW", self.onExit)

    def showMainScreen(self): # funkcija, lai izsauktu galveno ekrānu (Main Menu)
        if self.currentScreen: # Izdzēšam iepriekšējo ekrānu
            self.currentScreen.pack_forget()

    
        self.currentScreen = MainScreen(self) # izsauc MainScreen klasi
        self.currentScreen.pack()

    def showRulesScreen(self): # funkcija, lai izsauktu noteikumu ekrānu (Rules Screen)
        if self.currentScreen:
            self.currentScreen.pack_forget()

        self.currentScreen = RulesScreen(self)
        self.currentScreen.pack()
        
    def showSetupScreen(self): # funkcija, lai izsauktu iestatījumu ekrānu (Setup Screen)
        if self.currentScreen:
            self.currentScreen.pack_forget()

        self.humanRoundsWon = 0 # Aizejot uz Setup Screen, tiek atkal nodzēsti uzvaras punkti
        self.computerRoundsWon = 0
        self.currentScreen = SetupScreen(self)
        self.currentScreen.pack()

    def showNumberScreen(self, chosenAlgo, chosenPlayer, chosenDepth): # funkcija, kas izsauc ekrānu, kur izvēlās ciparus,
        # numberScreen, kur tiek padoti argumenti ar iepriekš (Setupā) izvēlētajiem parametriem
        if self.currentScreen:
            self.currentScreen.pack_forget()
        randNumbers = generate_numbers()  # uzģenerējam jaunus nejaušos skaitļus
        self.currentScreen = NumberScreen(self, randNumbers, chosenAlgo, chosenPlayer, chosenDepth, self.humanRoundsWon, self.computerRoundsWon) # izsaucam klasi NumberScreen,
        # kur līdzi klāt iepriekšējiem argumentiem arī nododam informāciju par uzvarēto raundu skaitu
        self.currentScreen.pack()
    
    def playGame(self, randNumber, chosenAlgo, chosenPlayer, chosenDepth, humanRoundsWon, computerRoundsWon): # funkcija priekš galvenā spēlēšanas ekrāna,
        # padodam argumentus ar setupā un skaitļu izvēles ekrānā izvēlētajiem parametriem
        if self.currentScreen:
            self.currentScreen.pack_forget()

        self.currentScreen = PlayGame(self, randNumber, chosenAlgo, chosenPlayer, chosenDepth, humanRoundsWon, computerRoundsWon) # padodam iepriekš minētos parametrus PlayGame klasei
        self.currentScreen.pack(fill="both", expand=True)

    def onExit(self): # funkcija, ja nospiež augšējās labās puses krustiņu tiek paprasīts, vai tiešām vēlas iziet, nospiežot jā, tiek aizvērts viss logs
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.destroy()
    
    def onRestart(self): # funkcija, ja nospiež Restart pogu tiek paprasīts, vai tiešām vēlas restartēt, nospiežot jā, atpakaļ atgriezts iestatījumu logs
        if messagebox.askyesno(title="Restart?", message="Do you really want to restart the game?"):
            self.showSetupScreen()
    
    def onReturnMain(self): # funkcija, ja nospiež Exit to Main Menu pogu tiek paprasīts, vai tiešām vēlas iziet, nospiežot jā, atpakaļ atgriezts galvenais ekrāns (Main menu)
        if messagebox.askyesno(title="Return to Menu?", message="Do you really want to return back to Main Menu?"):
            self.showMainScreen()


class MainScreen(tk.Frame): # Klase galvenajam ekrānam
    def __init__(self, master): # inicializē self un master parametrus 
        tk.Frame.__init__(self, master)

        # Uzraksts
        self.title = tk.Label(self, text="Welcome to THE GAME", font=("Arial", 18)) 
        self.title.pack()

        # Pogas
        self.buttonStart = tk.Button(self, text="Start Game", font=("Arial", 14), command=master.showSetupScreen)
        self.buttonStart.pack(pady=25)

        self.buttonRules = tk.Button(self, text="Rules", font=("Arial", 14), command=master.showRulesScreen)
        self.buttonRules.pack(pady=25)

        self.buttonExit = tk.Button(self, text="Exit", font=("Arial", 14), command=master.onExit)
        self.buttonExit.pack(pady=25)


class RulesScreen(tk.Frame): # Klase noteikumu ekrānam
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.frameRules = tk.Frame(self, width=master.screenWidth, height=master.screenHeight) # Izveidojam jaunu rāmi ekrānam, lai neveidotos šis ekrāns blakus iepriekšējam 
        self.frameRules.pack()

        ruleText = '''
                    Spēles sākumā ir dots cilvēka-spēlētāja izvēlētais skaitlis.
                    Kopīgs punktu skaits ir vienāds ar 0 (punkti netiek skaitīti katram spēlētājam atsevišķi).
                    Turklāt spēlē tiek izmantota spēles banka, kura sākotnēji ir vienāda ar 0.
                    Spēlētāji izdara gājienus pēc kārtas, katrā gājienā dalot pašreizējā brīdī esošu skaitli ar 3,4 vai 5.
                    Skaitli ir iespējams sadalīt tikai gadījumā, ja rezultātā veidojas vesels skaitlis.
                    Ja dalīšanas rezultātā veidojas pāra skaitlis, tad kopīgajam punktu skaitam tiek pieskaitīts 1 punkts.
                    Savukārt, ja tiek iegūts skaitlis, kas beidzās ar 0 vai 5, tad bankai tiek pieskaitīts 1 punkts.
                    Spēle beidzas, kad iegūto skaitli vairs nav iespējams sadalīt. Ja kopīgais punktu skaits ir pāra skaitlis,
                    tad no tā atņem bankā uzkrātos punktus. Ja tas ir nepāra skaitlis, tad tam pieskaita bankā uzkrātos punktus.
                    Ja kopīgā punktu skaita gala vērtība ir pāra skaitlis, uzvar spēlētājs, kas uzsāka spēli, ja nepāra skaitlis,
                    tad otrais spēlētājs.
                   '''
        self.rulesText = tk.Label(self.frameRules, text=ruleText, font=("Arial", 12))
        self.rulesText.pack(pady=50)

        self.buttonBack = tk.Button(self, text="Back to Main Screen", font=("Arial", 14), command=master.showMainScreen)
        self.buttonBack.pack(pady=50)


class SetupScreen(tk.Frame): # Iestatījumu ekrāna klase, šeit tiek iegūtas no lietotāja spēles opcijas, kādās vēlās spēlēt
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frameRules = tk.Frame(self, width=master.screenWidth, height=master.screenHeight) # jauns rāmis, lai neveidotos blakus iepriekšējā informācija
        self.frameRules.pack()

        # Algoritma izvēle
        self.algoFrame = tk.LabelFrame(self.frameRules, text="Choose the algorithm", font=("Arial", 14))
        self.algoFrame.pack(pady=5, padx=5, anchor='center',fill='x')

        self.varAlgo = tk.StringVar(value="MiniMax")
        self.radioAlgorithm = tk.Radiobutton(self.algoFrame, text="MiniMax", font=("Arial", 14), variable=self.varAlgo, value="MiniMax")
        self.radioAlgorithm.pack(side='left',padx=(60,0), pady=5, anchor='center')

        self.radioAlgorithm = tk.Radiobutton(self.algoFrame, text="Alpha-Beta", font=("Arial", 14), variable=self.varAlgo, value="AlphaBeta")
        self.radioAlgorithm.pack(side='right',padx=(0,60), pady=5, anchor='center')

        # Pirmā spēlētāja izvēle
        self.playerFrame = tk.LabelFrame(self.frameRules, text="Choose the first player", font=("Arial", 14))
        self.playerFrame.pack(pady=5, padx=5, anchor='center',fill='x')

        self.varPlayer = tk.StringVar(value="Human")
        self.radioPlayer = tk.Radiobutton(self.playerFrame, text="Human", font=("Arial", 14), variable=self.varPlayer, value="Human")
        self.radioPlayer.pack(side='left',padx=(60,0), pady=5, anchor='center')

        self.radioPlayer = tk.Radiobutton(self.playerFrame, text="Computer", font=("Arial", 14), variable=self.varPlayer, value="Computer")
        self.radioPlayer.pack(side='right',padx=(0,60), pady=5, anchor='center')
        
        # Spēles koka ģenerēšanas dziļuma izvēle, vai arī pilna koka ģenerēšanas izvēle (noklusējums ar dziļumu 3)
        self.treeFrame = tk.LabelFrame(self.frameRules, text="Search Depth", font=("Arial", 14))
        self.treeFrame.pack(pady=5, padx=5, anchor='center',fill='x')
        self.varTree = tk.StringVar(value="Full tree")

        self.radioTree = tk.Radiobutton(self.treeFrame, text='Full tree', font=("Arial", 14), variable=self.varTree, value="Full tree", command=self.toggle_tree_input)
        self.radioTree.pack(side='left', padx=(5, 0), pady=5)

        self.radioTree = tk.Radiobutton(self.treeFrame, text='Depth of :', font=("Arial", 14), variable=self.varTree, value="Depth", command=self.toggle_tree_input)
        self.radioTree.pack(side='left', padx=(5, 10), pady=5)

        #Koka dziļuma izvēles ievades laukums
        self.treeInput = tk.Entry(self.treeFrame, font=("Arial", 14), width=10)
        self.treeInput.pack(side='left', padx=(0, 5), pady=5)
        self.treeInput.insert(tk.END, "3")

        self.errorLabel = tk.Label(self.frameRules, text="", font=("Arial", 14), fg="red")
        self.errorLabel.pack(pady=5, padx=5, anchor='center')

        # Poga, kas padod parametrus no iestatījumu ekrāna uz skaitļu izvēlni
        # master.showNumberScreen(izvēlētaisAlgoritms, izvēlētaisSpēlētājs, izvēlētaisDziļums) #shim ari ta japaliek
        self.buttonConfirm = tk.Button(self, text="Start", font=("Arial", 14), command=lambda: master.showNumberScreen(self.varAlgo.get(), self.getDepthInput(self.varPlayer.get()), int(self.treeInput.get()) if self.varTree.get() == "Depth" else "Full"))
        self.buttonConfirm.pack(pady=10)
        # Uz main menu
        self.buttonBack = tk.Button(self, text="Back to Main Screen", font=("Arial", 14), command=master.showMainScreen)
        self.buttonBack.pack(pady=10)

        # ChatGPT :  Iedots SetupScreen klases kods un paprasīts "can you modify this code, so when the depth option is selected, 
        # an input text box appears next to it with a default value 3 and it is editable,
        # but if that option is not selected, (the option full tree is selected) then that text box dissapears"
        # https://chat.openai.com/share/0e526414-7949-43f3-b7d8-ddb5620b7d28
        self.toggle_tree_input()  # Call to initially set the visibility based on the default selected option

        

    def toggle_tree_input(self):
        if self.varTree.get() == "Depth":
            self.treeInput.config(state='normal')
        else:
            self.treeInput.config(state='disabled')
        #...ChatGPT
        
    def getDepthInput(self, input):
        print(input)
        try:
            self.errorLabel.config(text="")
            input = int(input)
            return input
        except:
            self.errorLabel.config(text="Input must be an integer")
            return input


class NumberScreen(tk.Frame): # klase Priekš sākuma skaitļa izvēles
    def __init__(self, master, randNumbers, chosenAlgo, chosenPlayer, chosenDepth, humanRoundsWon, computerRoundsWon): # inicializējam iedotos parametrus
        tk.Frame.__init__(self, master)

        # Izveidojam šīs instances mainīgos no padotajiem argumentiem
        self.randNumbers = randNumbers
        self.chosenAlgo = chosenAlgo
        self.chosenPlayer = chosenPlayer
        self.chosenDepth = chosenDepth
        self.humanRoundsWon = humanRoundsWon
        self.computerRoundsWon = computerRoundsWon

        self.frameRules = tk.Frame(self, width=master.screenWidth, height=master.screenHeight) # jauns rāmis
        self.frameRules.pack()

        # Uzskaitīt raundu uzvaras
        self.roundsFrame = tk.LabelFrame(self.frameRules, text="Rounds won", font=("Arial", 14))
        self.roundsFrame.pack(pady=5, padx=5, anchor='n')
        self.roundsWonHumanLabel = tk.Label(self.roundsFrame, text="Human : " + str(self.humanRoundsWon), font=("Arial", 14))
        self.roundsWonHumanLabel.pack(pady=5)
        self.roundsWonComputerLabel = tk.Label(self.roundsFrame, text="Computer : " + str(self.computerRoundsWon), font=("Arial", 14))
        self.roundsWonComputerLabel.pack(pady=5)


        # Ģenerēto skaitļu izvēle
        self.rulesText = tk.Label(self.frameRules, text="Choose 1 of the numbers", font=("Arial", 14))
        self.rulesText.pack(pady=10)

        # Tabula ar skaitļu pogām
        buttonFrame = tk.Frame(self.frameRules)
        buttonFrame.columnconfigure(0, weight=1)
        buttonFrame.columnconfigure(1, weight=1)
        buttonFrame.columnconfigure(2, weight=1)
        buttonFrame.columnconfigure(3, weight=1)
        buttonFrame.columnconfigure(4, weight=1)
        # Ar ciklu izveidots pogu teksts un pogas komandas izsaukšana, lai pārietu uz galveno spēles ekrānu (PlayGame), padodam izveletos parametrus:
        btn_texts = [str(num) for num in self.randNumbers]  
        buttons = []
        for i in range(5):
            # master.playGame(izvēlētaisĢenerētaisSkaitlis, izvēlētaisAlgoritms, izvēlētaisSpēlētājs, izvēlētaisDziļums, cilvēkaUzvarētieRaundi, datoraUzvarētieRaundi)
            btn = tk.Button(buttonFrame, text=btn_texts[i], font=("Arial", 10), command=lambda idx=i: master.playGame(self.randNumbers[idx], self.chosenAlgo, self.chosenPlayer, self.chosenDepth, self.humanRoundsWon, self.computerRoundsWon))
            buttons.append(btn)
            btn.grid(row=0, column=i, padx=5, pady=5)
        
        buttonFrame.pack(fill="x", padx=50)

        self.buttonBack = tk.Button(self, text="Back to Main Screen", font=("Arial", 14), command=master.onReturnMain)
        self.buttonBack.pack(pady=50)

class PlayGame(tk.Frame): # Galvenā spēlēšanas ekrāna klase.
    def __init__(self, master, randNumber, chosenAlgo, chosenPlayer, chosenDepth, humanRoundsWon, computerRoundsWon): # inicializējam visus vajadzīgos parametrus no NumberScreen un SetupScreen
        tk.Frame.__init__(self, master)
        global firstPlayer
        global current_depth

        # Izveido instances mainīgos no padotajiem parametriem
        self.bankPoints = 0 # Inicializējam bankas punktus
        self.humanRoundsWon = humanRoundsWon
        self.computerRoundsWon = computerRoundsWon
        self.totalPoints = 0 # inicializējam Kopējos punktus
        self.currentNumber = int(randNumber)
        self.currentPlayer = chosenPlayer
        self.tree = Tree(int(self.currentNumber),0,0,0)
        self.tree.print_tree()
        firstPlayer = chosenPlayer
        # self.randNumber = randNumber
        self.chosenAlgo = chosenAlgo
        self.chosenDepth = chosenDepth
        current_depth = 0

        self.frameRules = tk.Frame(self, width=master.screenWidth, height=master.screenHeight) # Ģenerē jaunu ekrānu
        self.frameRules.pack() # Ģenerētais ekrāns tiek inicializēts

        #Raundu uzvaru uzskaite
        self.roundsFrame = tk.LabelFrame(self.frameRules, text="Rounds won", font=("Arial", 14))
        self.roundsFrame.pack(pady=5, padx=5, anchor='n')
        self.roundsWonHumanLabel = tk.Label(self.roundsFrame, text="Human : " + str(self.humanRoundsWon), font=("Arial", 14))
        self.roundsWonHumanLabel.pack(pady=5)
        self.roundsWonComputerLabel = tk.Label(self.roundsFrame, text="Computer : " + str(self.computerRoundsWon), font=("Arial", 14))
        self.roundsWonComputerLabel.pack(pady=5)

        # iepriekš izvēlētie spēles noteikumi
        self.startingFrame = tk.LabelFrame(self.frameRules, text="Chosen game settings", font=("Arial", 14))
        self.startingFrame.pack(pady=5, padx=5, anchor = "n", side = "left")
        self.startingNumber = tk.Label(self.startingFrame, text="Starting Number : " + str(randNumber), font=("Arial", 14))
        self.startingNumber.pack(pady=5)
        self.startingAlgo = tk.Label(self.startingFrame, text="Algorithm : " + str(chosenAlgo), font=("Arial", 14))
        self.startingAlgo.pack(pady=5)
        self.startingPlayer = tk.Label(self.startingFrame, text="Starting Player : " + str(chosenPlayer), font=("Arial", 14))
        self.startingPlayer.pack(pady=5)
        self.startingDepth = tk.Label(self.startingFrame, text="Game tree depth : " + str(chosenDepth), font=("Arial", 14))
        self.startingDepth.pack(pady=5)

        # Bankas un kopējo punktu skaitu uzskaite
        self.pointsFrame = tk.LabelFrame(self.frameRules, text="Points", font=("Arial", 14))
        self.pointsFrame.pack(pady=5, padx=5, anchor = "n", side = "left")
        self.totalPointsDisplay = tk.Label(self.pointsFrame, text="Total : " + str(self.totalPoints), font=("Arial", 14))
        self.totalPointsDisplay.pack(pady=5)
        self.bankPointsDisplay = tk.Label(self.pointsFrame, text="Bank : " + str(self.bankPoints), font=("Arial", 14))
        self.bankPointsDisplay.pack(pady=5)

        # Informācija par pašreizējo gājienu
        self.currentInfoFrame = tk.LabelFrame(self.frameRules, text="Turn information", font=("Arial", 14))
        self.currentInfoFrame.pack(pady=5, padx=5,anchor="s", fill='both', expand=True)
        self.currentMoveDisplay = tk.Label(self.currentInfoFrame, text="Current Move : " + str(self.currentPlayer), font=("Arial", 14))
        self.currentMoveDisplay.pack(pady=5)
        self.currentNumberDisplay = tk.Label(self.currentInfoFrame, text="Current number : " + str(self.currentNumber), font=("Arial", 16), fg='#f00')
        self.currentNumberDisplay.pack(pady=5)
        # Vesture gajieniem
        self.computerMoveDisplay = tk.Label(self.currentInfoFrame, font=("Arial", 8)) #text="Previous Move : " + str(self.prevMove)
        self.computerMoveDisplay.pack(pady=5)
        

        # 3 dalīšanas pogas
        buttonDividerFrame = tk.Frame(self.frameRules)
        buttonDividerFrame.columnconfigure(0, weight=1)
        buttonDividerFrame.columnconfigure(1, weight=1)
        buttonDividerFrame.columnconfigure(2, weight=1)
        # izsaucam, nospiežot pogas, funkciju, kur tiek atjaunināts ekrāns ar jauno informāciju
        # self.updateGameState(pašreizējieBankasPunkti, pašreizējaisSpēlētājs, pašreizējaisSkaitlisDalītsArDalītāju, kopējiePunkti)
        self.btn1 = tk.Button(buttonDividerFrame, text=":3", state='disabled', font=("Arial", 14), command= lambda: self.updateGameState(self.bankPoints, self.currentPlayer, int(self.currentNumber)//3, self.totalPoints))
        self.btn2 = tk.Button(buttonDividerFrame, text=":4", state='disabled', font=("Arial", 14), command= lambda: self.updateGameState(self.bankPoints, self.currentPlayer, int(self.currentNumber)//4, self.totalPoints))
        self.btn3 = tk.Button(buttonDividerFrame, text=":5", state='disabled', font=("Arial", 14), command= lambda: self.updateGameState(self.bankPoints, self.currentPlayer, int(self.currentNumber)//5, self.totalPoints))

        self.btn1.grid(row=0, column=0, padx=5, pady=5)
        self.btn2.grid(row=0, column=1, padx=5, pady=5)
        self.btn3.grid(row=0, column=2, padx=5, pady=5)

        buttonDividerFrame.pack(fill="x", padx=50)

        self.update_buttons_state() # funkcija, kur pārbauda vai var dalīt ar konkrēto dalītāju un attiecīgi izveido pogas nelietojamas vai lietojamas

        # Poga priekš nākamā raunda uzsākšanas
        self.buttonNextRound = tk.Button(self, text="Next Round", font=("Arial", 14), command=self.nextRound)
        self.buttonNextRound.config(state="disabled")
        self.buttonNextRound.pack(pady=5)

        self.buttonRestart = tk.Button(self, text="Restart Game", font=("Arial", 14), command=master.onRestart)
        self.buttonRestart.pack(pady=5)

        self.buttonBack = tk.Button(self, text="Back to Main Screen", font=("Arial", 14), command=master.onReturnMain)
        self.buttonBack.pack(pady=5)

        if firstPlayer == "Computer":
            self.computerFirstMove()


    def computerFirstMove(self): # ja dators iet pirmais, tad veic datora gajienu
        global elapsed_time
        global time_list
        if self.chosenAlgo == "MiniMax":
            if self.chosenDepth == "Full":
                #makeMove([0,kokaObjekts], True, False) # TODO
                new_current_number = makeMove([0,self.tree], True, False) # Aprēķinam jauno skaitli
                print('MiniMax Full izvelejas:', new_current_number)
                # Atjaunojam datora gajiena labelu UI
                self.computerMoveDisplay.config(text="Computer chose to divide " +  str(self.currentNumber) + " by " + str(int(self.currentNumber/int(new_current_number))))
                #Atjaunojam speles stavokli
                # self.updateGameState(pašreizējieBankasPunkti, pašreizējaisSpēlētājs, jaunaisAprēķinātaisSkaitlis, kopējiePunkti)
                self.updateGameState(self.bankPoints, self.currentPlayer, new_current_number, self.totalPoints)
            else:
                #makeMove([0,kokaObjekts], True, False) # TODO
                new_current_number = makeMoveDepth([0,self.tree], True, False, self.chosenDepth)
                print('MiniMax Depth izvelejas:', new_current_number)
                # Atjaunojam datora gajiena labelu UI
                self.computerMoveDisplay.config(text="Computer chose to divide " +  str(self.currentNumber) + " by " + str(int(self.currentNumber/int(new_current_number))))
                #Atjaunojam speles stavokli
                # self.updateGameState(pašreizējieBankasPunkti, pašreizējaisSpēlētājs, jaunaisAprēķinātaisSkaitlis, kopējiePunkti)
                self.updateGameState(self.bankPoints, self.currentPlayer, new_current_number, self.totalPoints)
        else:
            if self.chosenDepth == "Full":

                start_time = time.perf_counter_ns()
                # alphaBeta([0,kokaObjekts], Minimizetajs, alfa, beta)
                new_current_number = alphaBeta([0,self.tree], True, -math.inf, math.inf) #izsaucam alfa-beta
                end_time = time.perf_counter_ns()
                gameTime = (end_time - start_time)/ 1_000_000
                time_list.append(gameTime)
                elapsed_time = elapsed_time+gameTime
                
                new_current_number = new_current_number[1].value # jaunam skaitlim piešķir best_node vērtību no alfa-beta
                print('Alpha-Beta Full izvelejas:', new_current_number)
                self.computerMoveDisplay.config(text="Computer chose to divide " +  str(self.currentNumber) + " by " + str(int(self.currentNumber/int(new_current_number))))
                self.updateGameState(self.bankPoints, self.currentPlayer, new_current_number, self.totalPoints)
            else:
                start_time = time.perf_counter_ns()
                # alphaBeta([0,kokaObjekts], Minimizetajs,pašreizējaisDziļums, izvēlētaisDziļums, alfa, beta)
                new_current_number = alphaBetaWithDepth([0,self.tree], True, current_depth, self.chosenDepth, -math.inf, math.inf)
                end_time = time.perf_counter_ns()
                gameTime = (end_time - start_time)/ 1_000_000
                time_list.append(gameTime)
                elapsed_time = elapsed_time+gameTime
                new_current_number = new_current_number[1].value # jaunam skaitlim piešķir best_node vērtību no alfa-beta
                print('Alpha-Beta Depth izvelejas:', new_current_number)
                # atjaunina labels ui un speles stavokli
                self.computerMoveDisplay.config(text="Computer chose to divide " +  str(self.currentNumber) + " by " + str(int(self.currentNumber/int(new_current_number))))
                self.updateGameState(self.bankPoints, self.currentPlayer, new_current_number, self.totalPoints)

    def nextRound(self): # Sākam jaunu Raundu (mums būs jāizvēlās jauns pirmais skaitlis un opcijas paliek iepriekšējās)
        self.master.showNumberScreen(self.chosenAlgo, firstPlayer, self.chosenDepth)

    # ChatGPT : Iedots viss kods un paprasits "How can i make the class playGame update its numbers when i do a certain command?"
    # https://chat.openai.com/share/f61aac97-32be-4e82-9fb3-ca10dc81601e
    def update_buttons_state(self):
        currentNumber = int(self.currentNumber)
        if currentNumber % 3 == 0:
            self.btn1.config(state='normal')
        else:
            self.btn1.config(state='disabled')

        if currentNumber % 4 == 0:
            self.btn2.config(state='normal')
        else:
            self.btn2.config(state='disabled')

        if currentNumber % 5 == 0:
            self.btn3.config(state='normal')
        else:
            self.btn3.config(state='disabled')
#...chatgpt
    def checkIfGameOver(self): # Pārbauda, vai ir beigusies spēle un pieskaita punktus attiecīgajam spēlētājam pēc spēles noteikumiem
        global elapsed_time
        global time_list
        global skibidi_toilet
        global nodeCounter
        currentNumber = int(self.currentNumber)
        if currentNumber % 3 != 0 and currentNumber % 4 != 0 and currentNumber % 5 != 0:
            print("Game over")
            print("Total nodes visited:", nodeCounter)
            print("Total time spent:", elapsed_time)
            print("Average time spent per move:", sum(time_list)/len(time_list))
            # print(f'[{self.currentNumber}, {nodeCounter}, {time_list}, {str(sum(time_list)/len(time_list))}, {skibidi_toilet}]')
            nodeCounter = 0
            time_list = []
            elapsed_time = 0
            return True
        else:
            return False
    def calculateRoundPoints(self):
        if self.totalPoints % 2 == 0:
            self.totalPoints = self.totalPoints - self.bankPoints
        else:
            self.totalPoints = self.totalPoints + self.bankPoints
        text = self.startingPlayer.cget("text")
        startPlayer = text.split(" ")[3]
        if self.totalPoints % 2 == 0: 
            #print("The starting player (" + str(startPlayer) + ") has won.")
            winningPlayer = startPlayer
        else:
            otherPlayer = ""
            if startPlayer == "Human":
                otherPlayer = "Computer"
            else:
                otherPlayer = "Human"
            #print("The latter player (" + str(otherPlayer) + ") has won.")
            winningPlayer = otherPlayer
        if winningPlayer == "Human":
            self.humanRoundsWon = self.humanRoundsWon + 1
            #print("Rounds won by Human : " + str(self.humanRoundsWon))
        else:
            self.computerRoundsWon = self.computerRoundsWon + 1
            #print("Rounds won by Computer : " + str(self.computerRoundsWon))
        self.updateRoundsWon(self.humanRoundsWon, self.computerRoundsWon) # atjauno informāciju par raundu uzvarām
            
    def updateGameState(self, new_bank, current_player, new_current_number, new_total_points): # Atjaunojam spēles informāciju ekrānā un veicam totalPoints un bankPoints
        global elapsed_time
        global time_list
        global current_depth
        current_depth = current_depth + 1
        
        if current_player == "Human": # Šeit samainam informāciju, kuram spēlētājam ir gājiens
            current_player = "Computer"
            print("Human chose:", new_current_number)
        else:
            current_player = "Human"
        if int(new_current_number) % 2 == 0:
            new_total_points = new_total_points + 1
            # print("new_current_number is divisible by 2")
        else:
            new_total_points = new_total_points - 1
            # print("new_current_number is not divisible by 2")
        if int(new_current_number) % 5 == 0: # if last_digit == '0' or last_digit == '5':
            new_bank += 1
            # print("Last digit is 0 or 5. Adding 1 point to bank.")


        if isinstance(new_current_number, int):
            new_current_number = int(new_current_number)
        self.bankPoints = new_bank
        self.currentPlayer = current_player
        self.currentNumber = new_current_number
        self.totalPoints = new_total_points
        
        # jauno info iedodam ekrānam
        self.bankPointsDisplay.config(text="Bank : " + str(self.bankPoints))
        self.currentMoveDisplay.config(text="Current Move : " + self.currentPlayer)
        self.currentNumberDisplay.config(text="Current Number : " + str(self.currentNumber))
        self.totalPointsDisplay.config(text="Total : " + str(self.totalPoints))

        if current_player == "Computer": # Ja ir pienacis datora gajiens, izsaucam algoritmu ar parametriem, kuriem tika iestatita spele
            if self.checkIfGameOver() == True:
                self.calculateRoundPoints()
            else:
                if self.chosenAlgo == "MiniMax":
                    if self.chosenDepth == "Full":
                        #makeMove([0,kokaObjekts(int(pašreizējaisSkaitlis), kopējiePunkti, bankasPunkti,0)], True, False) # TODO
                        new_current_number = makeMove([0,Tree(int(self.currentNumber),self.totalPoints,self.bankPoints,0)], True, False)
                        print('MiniMax Full izvelejas:', new_current_number)
                        self.computerMoveDisplay.config(text="Computer chose to divide " +  str(self.currentNumber) + " by " + str(int(self.currentNumber/int(new_current_number))))
                        self.updateGameState(self.bankPoints, self.currentPlayer, new_current_number, self.totalPoints)
                    else:
                        #makeMoveDepth([0,kokaObjekts(int(pašreizējaisSkaitlis), kopējiePunkti, bankasPunkti,0)], True, False, izvēlētaisDziļums) # TODO
                        new_current_number = makeMoveDepth([0,Tree(int(self.currentNumber),self.totalPoints,self.bankPoints,0)], True, False, self.chosenDepth)
                        print('MiniMax Depth izvelejas:', new_current_number)
                        self.computerMoveDisplay.config(text="Computer chose to divide " +  str(self.currentNumber) + " by " + str(int(self.currentNumber/int(new_current_number))))
                        self.updateGameState(self.bankPoints, self.currentPlayer, new_current_number, self.totalPoints)
                else:
                    if self.chosenDepth == "Full":
                        start_time = time.perf_counter_ns()
                        # alphaBeta([0,kokaObjekts(int(pašreizējaisSkaitlis), kopējiePunkti, bankasPunkti,0)], Minimizetajs, alfa, beta)
                        new_current_number = alphaBeta([0,Tree(int(self.currentNumber),self.totalPoints,self.bankPoints,0)], True, -math.inf, math.inf)
                        end_time = time.perf_counter_ns()
                        gameTime = (end_time - start_time)/ 1_000_000
                        time_list.append(gameTime)
                        elapsed_time = elapsed_time+gameTime

                        new_current_number = new_current_number[1].value
                        print('Alpha-Beta Full izvelejas:', new_current_number)
                        self.computerMoveDisplay.config(text="Computer chose to divide " +  str(self.currentNumber) + " by " + str(int(self.currentNumber/int(new_current_number))))
                        self.updateGameState(self.bankPoints, self.currentPlayer, new_current_number, self.totalPoints)
                    else:
                        start_time = time.perf_counter_ns()
                        # alphaBeta([0,kokaObjekts(int(pašreizējaisSkaitlis), kopējiePunkti, bankasPunkti,0)], Minimizetajs ,pašreizējaisDziļums, izvēlētaisDziļums, alfa, beta)
                        new_current_number = alphaBetaWithDepth([0,Tree(int(self.currentNumber),self.totalPoints,self.bankPoints,0)], True, current_depth, self.chosenDepth, -math.inf, math.inf)
                        end_time = time.perf_counter_ns()
                        gameTime = (end_time - start_time)/ 1_000_000
                        time_list.append(gameTime)
                        elapsed_time = elapsed_time+gameTime

                        new_current_number = new_current_number[1].value
                        print('Alpha-Beta Depth izvelejas:', new_current_number)
                        self.computerMoveDisplay.config(text="Computer chose to divide " +  str(self.currentNumber) + " by " + str(int(self.currentNumber/int(new_current_number))))
                        self.updateGameState(self.bankPoints, self.currentPlayer, new_current_number, self.totalPoints)
        else:
            # self.checkIfGameOver() # pārbaudam, vai nav beigusies spēle
        
            if self.checkIfGameOver() == True:
                self.calculateRoundPoints()

        self.update_buttons_state() # paskatamies, vai kaut kas jādara ar pogām


    def updateRoundsWon(self, new_roundsWonHuman, new_roundsWonComputer): # funkcija, kura piešķir jaunās vērtības par raundu uzvaru un atļauj uzspiest pogu "Next Round"

   
        self.master.humanRoundsWon = new_roundsWonHuman
        self.master.computerRoundsWon = new_roundsWonComputer
        self.roundsWonHumanLabel.config(text="Human : " + str(new_roundsWonHuman))
        self.roundsWonComputerLabel.config(text="Computer : " + str(new_roundsWonComputer))
        self.buttonNextRound.config(state="active")

def generate_numbers(): # Ģenerējam skaitļus
    numbers = []
    while len(numbers) < 5:
        number = random.randint(40000, 50000)
        if (number % 3 == 0 and number % 4 == 0 and number % 5 == 0) and number not in numbers:
            numbers.append(number)
    return numbers

GraphicalUserInterface().mainloop() # Uzsākam Grafisko Interfeisu

# GUI izveides izmantotie materiāli un rīki :
# https://www.youtube.com/watch?v=ibf5cx221hk
# https://www.youtube.com/watch?v=3yeRcxkth0I
# https://github.com/maskottchentech/Python/blob/master/Tkinter_multiple_frames.py
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

# smeltas idejas arī no chatGPT :
# https://chat.openai.com/share/f61aac97-32be-4e82-9fb3-ca10dc81601e 
# https://chat.openai.com/share/efdd730f-bc05-4412-a681-62c37f9b44d3
# https://chat.openai.com/share/4c5b4a0e-c701-41c2-a12b-e7d31e2781af

# Par MiniMax algoritma darbību izklāsts:
# https://faithful-flute-ca2.notion.site/MiniMax-algoritma-skaidrojums-b2539d52b9f74c4697ea0bddc0860127
