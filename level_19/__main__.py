import email
import wave


def main():
    message = open('mail.txt', 'rb').read().decode()

    mail = email.message_from_string(message)

    audio = mail.get_payload(0).get_payload(decode=True)

    f = open('indian.wav', 'wb')
    f.write(audio)

    w = wave.open('indian.wav', 'rb')
    new_wav = wave.open('result.wav', 'wb')
    new_wav.setnchannels(w.getnchannels())
    new_wav.setsampwidth(w.getsampwidth() // 2)
    new_wav.setframerate(w.getframerate() * 2)
    frames = w.readframes(w.getnframes())
    wave.big_endiana = 1
    new_wav.writeframes(frames)
    new_wav.close()


if __name__ == '__main__':
    main()
