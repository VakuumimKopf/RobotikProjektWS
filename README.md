# **Robotik - Oliver Lorenz**

## **Belegaufgabe 1 (Publisher Subscriber)**
### **Funktionsweise**
Hierbei sollten zwei Packages erstellt werden. Dabei sollte eines Publisher (in C++) und eines Subscriber (in Python) sein.
Der Publisher ist dabei im Package cpp_pubsub zu finden und der Subscriber im Package timing_tubaf_py.
Beim ausführen beider Packages hat zur Folge, dass der Publisher auf einen bestimmten Topic "number" die ganze Zeit "Hello World!" überträgt, während der Subscriber auf diesem Topic diese Nachrichten empfängt und mit entsprechender Nummer wieder ausgibt. Zusätzlich published er auf dem Topic "diff" die Zeitdifferenz der letzten beiden Nachrichten auf "number" 

### **Startanleitung**
Zum ausführen öffnet man ein Terminal und navigiert in das Verzeichnis, welches die ros Packages enthält.
Anschließend führt man folgende Befehle aus:
- colcon build
- source install/local_setup.bash
- ros2 run cpp_pubsub talker
- ros2 run timing_tubaf_py listener

## **Belegaufgabe 2 (Laserfollow)**
### **Funktionsweise**
Hierbei sollte ein Package entwickelt werden welches in der Lage ist die Daten des Laserscanners auf dem Topic "scan" auszulesen. Mit diesen ausgelesenen Daten sollte nun in einem 60° Kegel vor dem Roboter das Objekt identifiziert werden, welches am nächsten ist und wie weit es entfernt ist. Dafür bestimmt das Package den kleinsten Eintrag im Array der Daten des Laserscaners, welcher sich immer gewünschten Kegel befindet. Das Array besteht dabei aus 360 Einträgen wobei jeder ein Grad abbildet und der erste Eintrag auf 0° liegt (also nach vorne in Fahrtrichtung). Um den 60° Kegel abzubilden werden also nur die ersten 30 Einträge und die letzten 30 betrachtet. Befindet sich der geringste Weert nun unter der ersten 30 Einträgen dreht sich der Roboter im Urzeigersinn, wohingegen der Roboter, falls der Eintrag in den letzten 30 Einträgen liegt, sich gegen den Urzeigersinn dreht. Der Roboter dreht sich so lange bis der niedrigste Eintrag auf dem 0. Eintrag liegt. Außerdem betrachtet der Roboter den konkreten Wert des niedrigsten Eintrages, wenn dieser ein bestimmtes Maß unterschreitet fährt der Roboter nicht mehr vorwärts, um nicht mit dem Objekt zusammenzustoßen. Anderenfalls fährt der Roboter mit gleicher Geschwindigkeit auf das Objekt zu.

### **Startanleitung**
Zum ausführen öffnet man ein Terminal und navigiert in das Verzeichnis, welches die ros Packages enthält.
Anschließend führt man folgende Befehle aus:
- colcon build
- source install/local_setup.bash
- ros2 run

Um sicherzustellen, dass das Package auf den Laserscaner zugreifen kann sollte vorher mittels "ros2 topic list" überprüft werden, ob das entsprechende Topic des Laserscaners existiert.

## **Belegaufgabe 3 (Linefollow)**
### **Funktionsweise**
Hierbei sollte ein Package entwickelt werden welches mittels der Daten der Kamera des Roboters einer weißen Linie auf dem Boden zu folgen. Dazu wird zunächst das Bild auf dem Topic "/image_raw/compressed" ausliest und in ein schwarz-weiß Bild konvertiert. Anschließend wird auch nur die unterste Reihe an Pixeln in diesem Bild betrachtet und von diesem Array der hellste Wert (höchste Wert) betrachet. Danach wird überprüft, ob dieser unter dem Lightlim liegt, wenn befindet sich keine Linie in Sicht und der Roboter bleibt stehen und dreht sich im Kreis. Nun werden die 20 hellsten Einträge ausgewertet und ihr Median gebildet und dessen Index im originall Array festgestellt, falls dieser Index nun kleiner als der mittlere Index des Arrays ist muss sich der Roboter nach Links drehen. Im anderen Fall muss sich er nach Rechts drehen.

### **Startanleitung**
Zum ausführen öffnet man ein Terminal und navigiert in das Verzeichnis, welches die ros Packages enthält.
Anschließend führt man folgende Befehle aus:
- colcon build
- source install/local_setup.bash
- ros2 launch linebounce_launch.py

## **Belegaufgabe 4 (Zwischen 2 Objekten auf einer Linie fahren)**
### **Funktionsweise**
Hierbei soll ein Package aus 3 Notes erstellt werden, welches dem Roboter ermöglicht einer weißen Linie zu folgen bis er auf ein Objekt trifft, an welchem er wendet um der selben Linie in die andere Richtung zu folgen bis er wieder auf ein Objekt trifft. Die Node laserturn verwaltet dabei die mittels des Laserscaners, ob der Roboter sich einem Objekt nähert und leitet dabei dann die Drehbewegung ein indem sie auf einem eigenen Topic "laser" eine Drehanweisung published. Ist die Drehung abgeschlossen published sie kein Drehbefehl mehr.
Die andere Note linefollow funktioniert genauso wie das Package aus Aufgabe 3, nur das hier der Fahrbefehl nicht direkt an den Roboter geschickt wird, sondern mittels des eigenen Topic "line" published. 
Die letzte Node die noch gebraucht wird ist der nodemaster dieser subscribed auf beiden Topics "laser" und "line" und erhält somit 2 verschiedene Fahranweisungen, wobei er entscheiden muss welchen er an den Roboter weiterleitet. Dies tut er indem er zwischen 3 Zuständen unterscheidet Follow, Turn und Error. Welcher Zustand gerade angenommen wird und somit welchen Fahrbefehl er weiterleitet, hängt von dem Fahrbefehl der Node laserturn ab. In ihr schaut er sich an, ob die Drehung auf Null ist oder nicht. Falls sie auf Null ist wechselt er in den Zustand follow und überträgt den Bewegungsbefehl aus dem Topic "line". Falls sie nicht Null ist wechselt er in den Zustand turn und überträgt den Fahrbefehl aus dem Topic "laser". 

### **Startanleitung**
Zum ausführen öffnet man ein Terminal und navigiert in das Verzeichnis, welches die ros Packages enthält.
Anschließend führt man folgende Befehle aus:
- colcon build
- source install/local_setup.bash
- ros2 launch two_drive two_drive_launch.py

