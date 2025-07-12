pip install mido python-rtmidi

from mido import Message, MidiFile, MidiTrack

# 1. 피보나치 수열 생성 함수
def fibonacci(n):
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

# 2. 수열을 MIDI 음계 번호로 변환
def scale_to_midi(seq, base=60, scale_range=12):
    return [base + (x % scale_range) for x in seq]

# 3. MIDI 파일 생성 함수
def create_midi(midi_notes, filename='sequence.mid', duration=480):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    for note in midi_notes:
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=duration))

    mid.save(filename)
    print(f"[✅ 저장 완료] {filename} 파일이 생성되었습니다.")

# 4. 전체 실행 흐름
def main():
    n = 20  # 수열 항 개수
    fib_seq = fibonacci(n)
    midi_notes = scale_to_midi(fib_seq, base=60, scale_range=12)
    create_midi(midi_notes, filename="fibonacci_music.mid")

if __name__ == "__main__":
    main()
