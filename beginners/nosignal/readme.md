# nosignal

## Description
n00b got to know that flag will be transmitted in a TV show. But unfortunately, n00b was only able too to get only two snapshots. Help him find the flag with the help of images a[http://hack.bckdr.in/NO-SIGNAL/a.jpg] and b[http://hack.bckdr.in/NO-SIGNAL/b.jpg]. Submit SHA-256 of the flag.
Created by: Amanpreet Singh
No. of Correct Submissions: 595

## Solution
Download the images and verify their filetypes.
```
$ wget http://hack.bckdr.in/NO-SIGNAL/a.jpg && wget http://hack.bckdr.in/NO-SIGNAL/b.jpg

$ file a.jpg && file b.jpg
a.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, progressive, precision 8, 800x300, frames 3
b.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 800x300, frames 3

```

Ok so it is two images. I tried to open them both with gimp, overlaying them and playing with the opacity settings. This gave me a clue to try and xor the images. We can do this with the gmic package.

```
$ gmic a.jpg b.jpg -blend xor -o result.png
```
Looking at the output gives us our flag, but the task tells us to submit a sha256 of the flag.

echo -n <flag> | sha256sum
