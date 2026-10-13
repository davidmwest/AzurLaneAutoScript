import numpy as np

from module.ocr.al_ocr import AlOcr


def test_shorter_images_of_a_batch_are_padded_with_background():
    ocr = AlOcr()
    text = np.zeros((1, 32, 10), dtype=np.float32)
    longer_text = np.zeros((1, 32, 25), dtype=np.float32)

    images, widths = ocr._pad_arrays([text, longer_text])

    assert widths == [10, 25]
    assert [image.shape for image in images] == [(1, 32, 25), (1, 32, 25)]
    assert np.all(images[0][:, :, :10] == 0)
    assert np.all(images[0][:, :, 10:] == 1)
    assert np.all(images[1] == 0)
