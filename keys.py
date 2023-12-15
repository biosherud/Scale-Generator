"""Scale Generator

https://exercism.org/tracks/python/exercises/scale-generator
"""


class Scale:
    """Generate a list of musical scales based on the given `tonic` value.

    https://en.wikipedia.org/wiki/Scale_(music)

    Parameters:
    ----------
    tonic:
        A string character representing the tonic scale to generate.

    Attributes:
    ----------
    tonic:
        A string character representing the tonic scale to generate.
    pitches:
        A list of strings representing the pitches in the `Scale` objects chromatic scale.
    tonic_index:
        An interger index for the `tonic` in `scale`.
    SHARP_PITCHES:
        A list of strings representing the standard 12 pitch chromatic scale with
        sharp(#) key signatures.
    FLAT_PITCHES:
        A list of strings representing the standard 12 pitch chromatic scale with
        flat(b) key signatures.
    SHARP_TONES:
        A list of strings that have a sharp(#) key signature.
    FLAT_TONES:
        A list of strings that have a flat(b) key signature.
    INTERVALS:
        A dictionary with {string: integer} pairs for each supported interval and it's
        value.

    Functions:
    ---------
    chromatic() -> list[str]:
        Return the chromatic scale of the `Scale` objects given `tonic`.
    interval(intervals: str) -> list[str]:
        Return a diatonic scale of the `Scale` objects `tonic`, with the given `intervals`.
    validate_tonic(tonic: str) -> str:
        Return a ValueError if `tonic` is invalid.
    validate_intervals(intervals: str) -> str:
        Return a ValueError if an invalid interval is supplied in `intervals`.

    Raises:
    ------
    ValueError:
        If an invalid `tonic` value is given.
        If an invalid interval is passed when calling `interval()`.
    """
    SHARP_PITCHES = "A   A#  B   C   C#  D   D#  E   F   F#  G   G#".split()
    FLAT_PITCHES = "A   Bb  B   C   Db  D   Eb  E   F   Gb  G   Ab".split()
    SHARP_TONES = "A   B   C   D   E   F#  G   a   b   c#  d#  e   f#  g#".split()
    FLAT_TONES = "Ab  Bb  Cb  Db  Eb  F   Gb  ab  bb  c   d   eb  f   g ".split()
    INTERVALS = {"m": 1, "M": 2, "A": 3}

    def __init__(self, tonic: str):
        self.tonic = self.validate_tonic(tonic)
        self.pitches = self.SHARP_PITCHES if tonic in self.SHARP_TONES else self.FLAT_PITCHES
        self.tonic_index = self.pitches.index(self.tonic.capitalize())

    def chromatic(self) -> list[str]:
        """Return the chromatic scale of the `Scale` objects given `tonic`."""
        return self.pitches[self.tonic_index:] + self.pitches[:self.tonic_index]

    def interval(self, intervals: str) -> list[str]:
        """Return a diatonic scale of the `Scale` objects `tonic`, with the given `intervals`."""
        i = self.tonic_index
        diatonic_scale = [self.pitches[i]]
        for interval in self.validate_intervals(intervals):
            i = (i + self.INTERVALS[interval]) % 12
            diatonic_scale.append(self.pitches[i])

        return diatonic_scale

    def major(self):
        i = self.tonic_index
        major_scale = [self.pitches[i]]
        for interval in ["M", "M", "m", "M", "M", "M", "m"]:
            i = (i + self.INTERVALS[interval]) % 12
            major_scale.append(self.pitches[i])

        basic = major_scale[0]
        fifth = major_scale[4]
        fourth = major_scale[3]
        second = major_scale[1]

        chords = f'{basic}, {fifth}, {fourth}, {second}'
        return major_scale, chords

    def minor(self):
        i = self.tonic_index
        minor_scale = [self.pitches[i]]
        for interval in ['M', 'm', 'M', 'M', 'm', 'M', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            minor_scale.append(self.pitches[i])

        basic = minor_scale[0] + 'm'
        fifth = minor_scale[4]
        fourth = minor_scale[3] + 'm'
        sixth = minor_scale[5]
        chords = f'{basic}, {fifth}, {fourth}, {sixth}'

        return minor_scale, chords


    def ousak(self):
        i = self.tonic_index
        ousak_scale = [self.pitches[i]]
        for interval in ['m','M','M','M','m','M','M']:
            i = (i + self.INTERVALS[interval]) % 12
            ousak_scale.append(self.pitches[i])

        basic = ousak_scale[0] + 'm'
        second = ousak_scale[1]
        third = ousak_scale[2]
        fourth = ousak_scale[3] + 'm'
        sixth = ousak_scale[5]
        seventh = ousak_scale[6] + 'm'
        chords = f'{basic}, {second}, {third}, {fourth}, {sixth}, {seventh}'

        return ousak_scale, chords

    def xitzaz(self):
        i = self.tonic_index
        xitzaz_scale = [self.pitches[i]]
        for interval in ['m','A','m','M','m','M','M']:
            i = (i + self.INTERVALS[interval]) % 12
            xitzaz_scale.append(self.pitches[i])

        basic = xitzaz_scale[0]
        second = xitzaz_scale[1]
        fourth = xitzaz_scale[3]
        seventh = xitzaz_scale[6]

        chords = f'{basic}, {second}, {fourth}, {seventh}'

        return xitzaz_scale, chords


    def armoniko(self):
        i = self.tonic_index
        armoniko_scale = [self.pitches[i]]
        for interval in ['M','m','M','M','m','A','m']:
            i = (i + self.INTERVALS[interval]) % 12
            armoniko_scale.append(self.pitches[i])

        basic = armoniko_scale[0] + 'm'
        fourth = armoniko_scale[3] + 'm'
        fifth = armoniko_scale[4]
        sixth =  armoniko_scale[5]

        chords = f'{basic}, {fourth}, {fifth}, {sixth}'

        return armoniko_scale, chords


    def sampax(self):
        i = self.tonic_index
        sampax_scale = [self.pitches[i]]
        for interval in ['M', 'm', 'm', 'A', 'm', 'M', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            sampax_scale.append(self.pitches[i])

        basic = sampax_scale[0] + 'm'
        third = sampax_scale[2]
        fifth = sampax_scale[4] + 'm'
        sixth = sampax_scale[5]

        chords = f'{basic}, {third}, {fifth}, {sixth}'

        return sampax_scale, chords


    def xitzaskiar(self):
        i = self.tonic_index
        xitzaskiar_scale = [self.pitches[i]]
        for interval in ['m', 'A', 'm', 'M', 'm', 'A', 'm']:
            i = (i + self.INTERVALS[interval]) % 12
            xitzaskiar_scale.append(self.pitches[i])

        basic = xitzaskiar_scale[0]
        second = xitzaskiar_scale[1]
        fourth = xitzaskiar_scale[3] + 'm'

        chords = f'{basic}, {second}, {fourth}'

        return xitzaskiar_scale, chords


    def niavent(self):
        i = self.tonic_index
        niavent_scale = [self.pitches[i]]
        for interval in ['M', 'm', 'A', 'm', 'm', 'A', 'm']:
            i = (i + self.INTERVALS[interval]) % 12
            niavent_scale.append(self.pitches[i])

        basic = niavent_scale[0] + 'm'
        fifth = niavent_scale[4]
        sixth = niavent_scale[5]

        chords = f'{basic}, {fifth}, {sixth}'

        return niavent_scale, chords

    def kartsigiar(self):
        i = self.tonic_index
        kartsigiar_scale = [self.pitches[i]]
        for interval in ['M', 'm', 'M', 'm', 'A', 'm', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            kartsigiar_scale.append(self.pitches[i])

        basic = kartsigiar_scale[0] + 'm'
        second = kartsigiar_scale[1] + 'm'
        fourth = kartsigiar_scale[3]
        seventh = kartsigiar_scale[6]

        chords = f'{basic}, {second}, {fourth}, {seventh}'

        return kartsigiar_scale, chords

    def peiraiotikos(self):
        i = self.tonic_index
        peiraiotikos_scale = [self.pitches[i]]
        for interval in ['m', 'A', 'M', 'm', 'm', 'M', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            peiraiotikos_scale.append(self.pitches[i])

        basic = peiraiotikos_scale[0]
        second = peiraiotikos_scale[1]
        fourth = peiraiotikos_scale[3]

        chords = f'{basic}, {second}, {fourth}'

        return peiraiotikos_scale, chords

    def poimenikos(self):
        i = self.tonic_index
        poimenikos_scale = [self.pitches[i]]
        for interval in ['M', 'm', 'A', 'm', 'M', 'm', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            poimenikos_scale.append(self.pitches[i])

        basic = poimenikos_scale[0] + 'm'
        third = poimenikos_scale[2]
        fifth = poimenikos_scale[4] + 'm'

        chords = f'{basic}, {third}, {fifth}'

        return poimenikos_scale, chords

    def segiax(self):
        i = self.tonic_index
        segiax_scale = [self.pitches[i]]
        for interval in ['A', 'm', 'm', 'M', 'm', 'A', 'm']:
            i = (i + self.INTERVALS[interval]) % 12
            segiax_scale.append(self.pitches[i])

        basic = segiax_scale[0]
        chords = f'{basic}'

        return segiax_scale, chords

    def tampaxaniotikos(self):
        i = self.tonic_index
        tampaxaniotikos_scale = [self.pitches[i]]
        for interval in ['M', 'M', 'm', 'M', 'm', 'A', 'm']:
            i = (i + self.INTERVALS[interval]) % 12
            tampaxaniotikos_scale.append(self.pitches[i])

        basic = tampaxaniotikos_scale[0]
        fourth = tampaxaniotikos_scale[3]
        fifth = tampaxaniotikos_scale[4]

        chords = f'{basic}, {fourth}, {fifth}'

        return tampaxaniotikos_scale, chords

    def xouzam(self):
        i = self.tonic_index
        xouzam_scale = [self.pitches[i]]
        for interval in ['A', 'm', 'm', 'M', 'M', 'M', 'm']:
            i = (i + self.INTERVALS[interval]) % 12
            xouzam_scale.append(self.pitches[i])

        basic = xouzam_scale[0]
        fourth = xouzam_scale[3]

        chords = f'{basic}, {fourth}'

        return xouzam_scale, chords

    def xouseini(self):
        i = self.tonic_index
        xouseini_scale = [self.pitches[i]]
        for interval in ['M', 'M', 'm', 'M', 'M', 'm', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            xouseini_scale.append(self.pitches[i])

        basic = xouseini_scale[0]
        second = xouseini_scale[1] + 'm'
        fifth = xouseini_scale[4] + 'm'
        sixth = xouseini_scale[5] + 'm'
        fourth = xouseini_scale[3]
        seventh = xouseini_scale[6]

        chords = f'{basic}, {second}, {fifth}, {sixth}, {fourth}, {seventh}'

        return xouseini_scale, chords

    def rast(self):
        i = self.tonic_index
        rast_scale = [self.pitches[i]]
        for interval in ['M', 'M', 'm', 'M', 'M', 'M', 'm']:
            i = (i + self.INTERVALS[interval]) % 12
            rast_scale.append(self.pitches[i])

        basic = rast_scale[0]
        fourth = rast_scale[3]
        fifth = rast_scale[4]
        second = rast_scale[1]

        chords = f'{basic}, {second}, {fifth}, {fourth}'

        return rast_scale, chords

    def kiournti(self):
        i = self.tonic_index
        kiournti_scale = [self.pitches[i]]
        for interval in ['M', 'm', 'M', 'M', 'M', 'm', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            kiournti_scale.append(self.pitches[i])

        basic = kiournti_scale[0] + 'm'
        second = kiournti_scale[1] + 'm'
        fourth = kiournti_scale[3]
        third = kiournti_scale[2]
        seventh = kiournti_scale[6]
        fifth = kiournti_scale[4] + 'm'

        chords = f'{basic}, {second}, {fifth}, {fourth}, {third}, {seventh}'

        return kiournti_scale, chords

    def lokrikos(self):
        i = self.tonic_index
        lokrikos_scale = [self.pitches[i]]
        for interval in ['m', 'M', 'M', 'm', 'M', 'M', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            lokrikos_scale.append(self.pitches[i])

        basic = lokrikos_scale[0] + 'm'
        second = lokrikos_scale[1]
        fourth = lokrikos_scale[3] + 'm'
        seventh = lokrikos_scale[6] + 'm'
        sixth = lokrikos_scale[5]

        chords = f'{basic}, {second}, {fourth}, {sixth}, {seventh}'

        return lokrikos_scale, chords

    def ludikos(self):
        i = self.tonic_index
        ludikos_scale = [self.pitches[i]]
        for interval in ['M', 'M', 'M', 'm', 'M', 'M', 'm']:
            i = (i + self.INTERVALS[interval]) % 12
            ludikos_scale.append(self.pitches[i])

        basic = ludikos_scale[0]
        fifth = ludikos_scale[4]
        sixth = ludikos_scale[5]

        chords = f'{basic}, {sixth}, {fifth}'

        return ludikos_scale, chords


    def mixoludikos(self):
        i = self.tonic_index
        mixoludikos_scale = [self.pitches[i]]
        for interval in ['M', 'M', 'm', 'M', 'M', 'm', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            mixoludikos_scale.append(self.pitches[i])

        basic = mixoludikos_scale[0]
        second = mixoludikos_scale[1] + 'm'
        fourth = mixoludikos_scale[3]
        seventh = mixoludikos_scale[6]
        sixth = mixoludikos_scale[5] + 'm'
        fifth = mixoludikos_scale[4] + 'm'


        chords = f'{basic}, {sixth}, {fifth}, {second}, {fourth}, {seventh}'

        return mixoludikos_scale, chords

    def ouzal(self):
        i = self.tonic_index
        ouzal_scale = [self.pitches[i]]
        for interval in ['m', 'A', 'm', 'M', 'M', 'm', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            ouzal_scale.append(self.pitches[i])

        basic = ouzal_scale[0]
        fourth = ouzal_scale[3]
        seventh = ouzal_scale[6] + 'm'

        chords = f'{basic}, {fourth}, {seventh}'
        return ouzal_scale, chords

    def souzinak(self):
        i = self.tonic_index
        souzinak_scale = [self.pitches[i]]
        for interval in ['M', 'm', 'A', 'm', 'm', 'M', 'M']:
            i = (i + self.INTERVALS[interval]) % 12
            souzinak_scale.append(self.pitches[i])

        basic = souzinak_scale[0] + 'm'
        third = souzinak_scale[2]
        fifth = souzinak_scale[4] + 'm'
        sixth = souzinak_scale[5]

        chords = f'{basic}, {third}, {fifth}, {sixth}'
        return souzinak_scale, chords


    def validate_tonic(self, tonic: str) -> str:
        """Return a ValueError if `tonic` is invalid."""
        if tonic not in self.SHARP_TONES + self.FLAT_TONES:
            raise ValueError("Invalid tonic value provided for `Scale` object.")
        return tonic

    def validate_intervals(self, intervals: str) -> str:
        """Raise a ValueError if an invalid interval is supplied in `intervals`."""
        if not any(i in self.INTERVALS for i in intervals):
            raise ValueError("Only intervals 'm', 'M', and 'A' are supported.")
        return intervals


    def scale_all(self):
        scales = {
            'Major': self.major(),
            'Minor': self.minor(),
            'Ousak': self.ousak(),
            'Xitzaz': self.xitzaz(),
            'Armoniko': self.armoniko(),
            'Sampax': self.sampax(),
            'Xitzaskiar': self.xitzaskiar(),
            'Niavent': self.niavent(),
            'Kartsigiar': self.kartsigiar(),
            'Peiraiotikos': self.peiraiotikos(),
            'Poimenikos': self.poimenikos(),
            'Segiax': self.segiax(),
            'Tampaxaniotikos': self.tampaxaniotikos(),
            'Xouzam': self.xouzam(),
            'Xouseini': self.xouseini(),
            'Rast': self.rast(),
            'Kiournti': self.kiournti(),
            'Lokrikos': self.lokrikos(),
            'Ludikos': self.ludikos(),
            'Mixoludikos': self.mixoludikos(),
            'Ouzal': self.ouzal(),
            'Souzinak': self.souzinak(),
        }

        return scales

