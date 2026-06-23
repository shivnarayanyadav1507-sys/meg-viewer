# Methodology of the Annual Mosaics used in the  Meghalaya Viewer (2015–2025)

Mosaics are composite images stacked and accumulated from multiple satellite scenes/tiles to represent a given year. For the viewer , the annual mosaics were generated for 2015, 2016, 2017, 2018, 2019, and 2020, mainly to support visual interpretation and therefore, assisting in building a historical, temporal viewer for Meghalaya. This was carried out primarily in Google Earth Engine (GEE) for collecting and filtering data, and in QGIS for post-processing.

Hence, the methodology was identical for the years 2016–2020 and 2025, as these all used Sentinel-2 datasets. Only the year 2015 was the exception, mainly because Sentinel-2 was not fully operational yet during 2015, therefore, Landsat 8 was used. Additionally, because Meghalaya is heavily covered with clouds, only the dry-season months were used for mosaicking across all the years.

Therefore, the methodology is as follows.

## Contents

- [2015 Mosaic (Landsat 8)](#2015-mosaic-landsat-8)
- [2016–2020 and 2025 Mosaic (Sentinel-2)](#20162020-and-2025-mosaic-sentinel-2)
  - [Year-specific notes](#year-specific-notes)
- [NDVI (2015–2020)](#ndvi-20152020)
- [Summary table](#summary-table)
- [Processing flow at a glance](#processing-flow-at-a-glance)
- [LISS-4 2025 Mosaic](#liss-4-2025-mosaic)

---

## 2015 Mosaic (Landsat 8)

The 2015 mosaic was done in GEE and was collected from Landsat 8 OLI, Collection 2, Tier 1, Level 2 surface reflectance. In GEE it can be called from `LANDSAT/LC08/C02/T1_L2`. So, the mentioned abbreviations, such as Tier 1 (T1), denote the best-quality, georeferenced scenes, and Level 2 (L2) denotes surface reflectance, meaning the imagery has been atmospherically corrected and is not TOA (which provides raw atmosphere data). Therefore, the effects of the atmosphere have been removed, leaving only the light reflected from the ground.

In regards to Landsat 8, it has a 16-day revisit cycle, hence giving one or either two usable scenes per month, especially over a cloudy region like Meghalaya. Therefore, this sparse coverage needed a wider acquisition window than the Sentinel-2 years to gather enough cloud-free scenes and not include gaps. The window therefore widden from late 2014 (December 2014) along with the pre-monsoon months (January to April 2015) and post-monsoon months (October–December 2015). Including late 2014 helped fill gaps and had minimum clouds, therefore providing a minimum-cloud, cloud-free mosaic.

Secondly, after the acquisition of the scenes, cloud masking was performed using the `QA_PIXEL` quality band, which flags and masks cloud, cloud shadow, dilated cloud, and cirrus based on per-pixel values. So, rather than filtering whole scenes by cloud percentage like in Sentinel data, all the available scenes were included, and cloud-affected pixels were masked out individually before compositing.

Thirdly, Landsat's surface reflectance was scaled to its true physical range using the product's scale factor and offset: Thus,

```
ρ = (DN × 0.0000275) − 0.2
```

where ρ is reflectance and DN is the stored integer value.

Fourthly, all the masked scenes were then stacked, and for mosaicking, a median composite was computed for each pixel where the middle value across all clear observations was taken. No averaging (mean) was applied, mainly because the median avoids and rejects haze and cloud-edge outliers, producing a cleaner and more seamless  composite.

Finally, due to Landsat 8 being of a 30 m resolution, pan-sharpening was done to enhance the spatial resolution up to 15 m. As we know, Landsat 8 has a panchromatic band (Band 8) which is at 15 m resolution. Hence, with the use of the HSV (Hue–Saturation–Value) pan-sharpening method, the true-colour composite was converted from RGB into HSV colour space. Basically, the 30 m true-colour image (Red, Green, Blue) is converted to Hue–Saturation–Value colour space:

```
(R, G, B) → (H, S, V)
```

The Value (brightness) channel is then replaced by the 15 m panchromatic band, and the image is converted back:

```
(H, S, V_pan) → (R′, G′, B′)
```

However, because the Landsat 8 panchromatic band covers only the visible spectrum and excludes the near-infrared, for vegetation indices such as NDVI the 30 m Landsat mosaic was used to generate the NDVI.

<img width="692" height="560" alt="image" src="https://github.com/user-attachments/assets/55e66f1e-4e39-4b8b-8065-ff790eb4e45a" />


---

## 2016–2020 and 2025 Mosaic (Sentinel-2)

From 2016 to 2020 and 2025, the methodology for all the mosaics is the same, with some small differences. Mainly, they were all generated from the Sentinel-2 Harmonized collection (`COPERNICUS/S2_SR_HARMONIZED`). This includes both Sentinel-2A and Sentinel-2B; what makes it best for such visuailisations is because the harmonized collection is preprocessed and has the same continuous radiometric processing across all years. Additionally, as compared to Landsat, Sentinel-2 has a more frequent revisit and therefore fewer gaps. Just like 2015, only the dry-season months were used, that is, the pre-monsoon (January–March) and post-monsoon (October–December) periods.

Therefore, as per the acquisition window, the first steps after collecting the scenes are cloud masking.

Hence, the first step of this was to filter the scenes by limiting the overall cloud cover using the `CLOUDY_PIXEL_PERCENTAGE`. For this work specifically, the threshold was set below 20%, except for 2019, which used 10% mainly due to heavy processing issues. Hence, the eligible scenes were collected, and further pixel-level cloud masking was applied through these two processes:

- The first process is the use of the **QA60 band**, which removes opaque clouds and cirrus. This process is possible because the QA60 band is inbuilt within each Sentinel-2 scene, in which the band flags the presence of opaque and cirrus clouds at the pixel level.
- Secondly, the **Scene Classification Layer (SCL)** was used to remove cloud shadow and any additional cloud. However, terrain shadow was not removed, as it occurs in the same locations every year.

Still, however, some haze over higher-elevation areas escaped, and even though haze subtraction was applied in post-processing, it yielded no improvement and instead created gaps, as those areas were partly visible and concentrated over high ground.

Additionally, because Sentinel-2 stores surface reflectance as an integer to save storage space rather than as its true decimal values, the surface reflectance was rescaled to its true 0–1 range by dividing by 10,000:

```
ρ = DN / 10000
```

Lastly, because the scenes were collected under different atmospheric conditions and sun angles, normalization had to be performed before compositing. Without it, brightness and contrast differences between scenes would appear, and seams would be quite prominent; therefore, the composite would not have a continuous appearance. Hence, the normalization was applied for each band, where a common brightness target was set from a reference median composite. The common target was obtained by first generating a median composite of all masked scenes, then computing its mean and standard deviation for each band over the entire study area (via a regional reduction). These per-band statistics defined the target brightness and contrast to which every individual scene was subsequently standardized. In GEE, `reduceRegion` was used to acquire the target brightness and contrast.

Therefore, each scene was then standardized so that its own mean and standard deviation matched the target, using the formula:

```
normalized = ((scene − scene_mean) / scene_std) × target_std + target_mean
```

As per the formula, the scene's own mean is subtracted, then the result is divided by the scene's standard deviation, then multiplied by the target standard deviation and added to the target mean. The result is a version of the scene where the mean and standard deviation are now equal to the targets, so all scenes share the same average brightness (mean) and contrast (standard deviation).

Thus, the normalized scenes were then combined using a median composite, like 2015, taking the middle value per pixel across all observations. Median was chosen over mean for its rejection of haze and cloud outliers, and it naturally fills gaps wherever a pixel was seen clearly on at least one date.

This methodology was applied identically to all the Sentinel-2 years, with the year-specific notes below.

<img width="628" height="624" alt="image" src="https://github.com/user-attachments/assets/16f37f1e-c237-4506-81f6-b76df5351320" />

### Year-specific notes

**2016**

The 2016 mosaic used only Sentinel-2A, because Sentinel-2B was not launched until March 2017. So the scenes of 2016 had a revisit of approximately 10 days, which means fewer scenes than the 2017–2020 years. Therefore, the 2016 mosaic had thinner coverage in the cloudiest zones, but even with a < 20% cloud threshold the gaps were all filled, and the processing flow was identical.

**2017, 2018, 2020, 2025**

The 2017 mosaic was the first full year with both Sentinel-2A and Sentinel-2B, acquiring data with a 5-day revisit and substantially more scenes than 2016, and were from the harmonised collection. So, consequently, 2017, 2018, 2020 and 2025 had no processing issues and all followed the same windows and cloud threshold (< 20%).

**2019**

2019 was the most cloud-affected and computationally heaviest year. The full-state 10 m export with normalization exceeded practical single-export limits in GEE, so 2019 was exported in two geographic halves (east and west) and mosaicked afterward in QGIS. Additionally, to reduce the processing and acquisition of more scenes, the cloud threshold was tightened to < 10%. Also, even though it was exported in halves, the normalization calculations were computed over the full state beforehand, so the two halves remained consistent with each other and with the other years.

---

## NDVI (2015–2020)

Lastly, for a complete mosaic and for a complete comparison, the Normalized Difference Vegetation Index (NDVI) of each year was generated, and it is derived as:

```
NDVI = (NIR − Red) / (NIR + Red)
```

In regards to Sentinel-2, it is `(B8 − B4) / (B8 + B4)`, and for Landsat 8 it is `(SR_B5 − SR_B4) / (SR_B5 + SR_B4)`.

Thus, NDVI ranges from −1 to +1, with dense vegetation being closer to +1. NDVIs were directly calculated and used for comparison between years from 2016 to 2020. However, in regards to 2015, NDVI was computed from the 30 m multispectral median composite, which has the near-infrared band. This cannot be done in the pan-sharpened L8 due to the removal of the NIR band.

---

## Summary table

| Year | Sensor | Revisit | Cloud threshold | Resolution | Composite | Normalization |
| --- | --- | --- | --- | --- | --- | --- |
| 2015 | Landsat 8 OLI (C2 L2) | 16 days | None | 30 m, later pan-sharpened to 15 m | Median | No |
| 2016 | Sentinel-2A only | 10 days | < 20% | 10 m | Median | Yes |
| 2017 | Sentinel-2A + 2B | 5 days | < 20% | 10 m | Median | Yes |
| 2018 | Sentinel-2A + 2B | 5 days | < 20% | 10 m | Median | Yes |
| 2019 | Sentinel-2A + 2B | 5 days | < 10% | 10 m | Median | Yes |
| 2020 | Sentinel-2A + 2B | 5 days | < 20% | 10 m | Median | Yes |
| 2025 | Sentinel-2A + 2B | 5 days | < 20% | 10 m | Median | Yes |

---

## Processing flow at a glance

**Landsat 8 (2015)**

1. **Landsat 8 scenes** — Dec 2014 + Jan–Apr + Oct–Dec 2015
2. **Cloud masking** — only `QA_PIXEL` used (cloud, shadow, dilated, cirrus)
3. **Rescale to surface reflectance** — `DN × 0.0000275 − 0.2`
4. **HSV pan-sharpening** — swaps the brightness (Value) for the 15 m pan band (TOA)
5. **Median composite (30 m)** — middle value per pixel across all scenes
6. **True-colour composite (15 m)** — for sharper visuals
7. **NDVI (30 m)** — from the Landsat 8 30 m composite

**Sentinel-2 (2016–2020, 2025)**

1. **Sentinel-2 scenes** — dry season: Jan–Mar + Oct–Dec
2. **Cloud-cover filter** — threshold < 20% (10% for 2019)
3. **Pixel cloud masking** — QA60 + SCL
4. **Rescale surface reflectance** — `DN ÷ 10,000` (0–1 range)
5. **Radiometric normalization** — match mean and std to median target
6. **Median composite (10 m)** — middle value per pixel
7. **NDVI layer** — `(B8 − B4) / (B8 + B4)`
8. **Export the mosaic**

---

## LISS-4 2025 Mosaic

For 2025, LISS 4 was also looked upon and mosaicked. So, the LISS-4 tiles/scenes were gathered from ResourceSat-2 and ResourceSat-2A LISS-4 Multispectral (Mx) imagery, which is provided by the Indian Space Research Organisation (ISRO) and freely available on Bhoonidhi (bhoonidhi.nrsc.gov.in).

| Parameter | Specification |
| --- | --- |
| Sensor | LISS-4 Multispectral (Mx), ResourceSat-2 and ResourceSat-2A |
| Spatial resolution | 5.8 m |
| Spectral bands | Band 1 Green (0.52–0.59 µm); Band 2 Red (0.62–0.68 µm); Band 3 NIR (0.77–0.86 µm) |
| Multispectral swath | 23–24 km |
| Systematic revisit (Mx) | 24 days (5 days achievable when sensor is steered to a target) |
| Data source | ISRO Bhoonidhi portal |
| Output CRS | UTM Zone 46N (WGS 84) |

The LISS-4 sensor provides three spectral bands at 5.8 m spatial resolution. Additionally, LISS-4 Mx has a narrow swath and coverage with a systematic multispectral revisit of approximately 24 days. Thus, for the year 2025, twenty scenes/tiles were acquired across multiple dates for Meghalaya. All tiles were selected from the dry periods (January–April and October–December), where cloud cover over Meghalaya is minimum.

### Cloud removal

Unlike Landsat and Sentinel-2, LISS-4 does not have a cloud-detection band or an automated cloud mask, because the sensor lacks the thermal and cirrus bands like Landsat (`QA_PIXEL`) and Sentinel-2 (QA60, SCL). At first, an automated spectral brightness threshold was evaluated as an alternative, but was rejected because the brightness thresholding removed bright land cover such as bare soil and did not do anything to capture the thin or light bright clouds.

Therefore, cloud and cloud-shadow areas were removed by manual work. For each acquisition date, cloud-affected areas were digitised as polygons and used to mask the corresponding pixels to NoData, removing them. Hence, other clear pixels from the other tiles from other acquisition dates filled those locations during the compositing stage. This manual approach, while more labour-intensive, provides reliable cloud removal for a sensor without an automated mask, and avoids the loss of valid bright ground that an automated threshold would incur. However, there were only 20 scenes and most months had only 1 tile each; hence, the removed clouded pixels had no replacements and almost every tile basically had clouds. Therefore, the final method was priority fill.

### Creating the mosaic

As mentioned, a priority-fill mosaic approach was adopted. Other reasons are that statistical compositing methods such as median (which was done for the Sentinel and Landsat mosaics) and maximum-greenest NDVI compositing were used but rejected. Median compositing blends all the 20 tiles to find the middle value; however, due to fewer tiles and in the presence of minor inter-scene misregistration, the pixels showed visible degradation and appeared blurry and misregistered.

Under the priority-fill approach, each tile was assigned a priority ranking, and the tiles were stacked such that the highest-priority clear pixel occupies each location on the state, overlapping the cloudy tiles; and at missing gaps, lower-priority tiles fill the gaps, principally cloud holes left by the tiles above them, and filling the missing coverage of the state.

Additionally, because every output pixel is derived from a single acquisition rather than a blend, this approach preserves the native 5.8 m sharpness of each contributing scene.

### Radiometric considerations

In regards to radiometric considerations, tile-to-tile differences in brightness and contrast are present in the composite. These mainly arose from the different acquisition dates, sun angles, and atmospheric conditions of the contributing scenes, and from the use of two source platforms.

Radiometric normalisation and histogram-based tonal matching were evaluated for the purpose of producing a tonally uniform display product. However, these adjustments provided no improvements, mainly due to the reduction in brightness, even though it removed the transparent white sheet. But still, even though the transparent sheet exists, the NDVI values were still realistic and consistent. Hence, to preserve the integrity of the index computation, the analysis uses the original pixel values. Additionally, Sentinel-2 was also used to make the 2025 mosaic separately.

### Conclusion

Therefore, the resulting mosaics, together with their corresponding NDVI layers, provide a clean, year-by-year record of land cover that can be used for visual interpretation and for tracking forest-cover change over time
