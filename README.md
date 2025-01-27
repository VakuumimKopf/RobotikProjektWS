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

