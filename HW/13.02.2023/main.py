import cv2

# Загрузка каскадного классификатора для распознавания лиц
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Загрузка видеофайла
cap = cv2.VideoCapture('video.mp4')

# Чтение кадров из видео и обработка их
while True:
    # Захват кадра из видео
    ret, frame = cap.read()

    # Преобразование кадра в оттенки серого для улучшения скорости обработки
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Поиск лиц на кадре
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Отрисовка прямоугольника вокруг обнаруженных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Отображение результата
    cv2.imshow('frame', frame)

    # Выход из цикла, если нажата клавиша 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
