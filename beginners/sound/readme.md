# sound

## Description
According to sources of n00b, west-side building of hackland contains a flag. n00b attacked the building of pros only to taste defeat. But n00b laid hands on a suspicious file[http://hack.bckdr.in/SOUND/sound.mp3]. Find the flag and submit it.
Created by: Amanpreet Singh
No. of Correct Submissions: 471

## Solution

Download the file & verify type.
```
$ wget http://hack.bckdr.in/SOUND/sound.mp3
$ file sound.mp3
sound.mp3: Audio file with ID3 version 2.4.0, extended header, contains: MPEG ADTS, layer III, v1, 128 kbps, 44.1 kHz, Monaural

```

Okay, so we can listen to the file with audacity.

```
$ audacity sound.mp3
```

It sounds like its reversed. Lets try and apply the reverse effect to it and see if that helps [sound_reversed.mp3]. It now seems to sound more like language, but way to fast. Lets try to slow it down 50% [sound_reversed_slowed].

"The flag is sha256 of upside_down"

```
$ echo -n upside_down | sha256sum
```

And we get our flag.
