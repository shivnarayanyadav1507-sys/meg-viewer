# User Guide - Meghalaya Historical Image Visualizer

Live viewer: <https://shivnarayanyadav1507-sys.github.io/meg-viewer/>

The Meghalaya Historical Image Visualizer runs entirely in any web browser, and its purpose is to assist in inspecting historical satellite imagery of Meghalaya (2015–2020), visualising the forest-cover change over time, as well alongside it visualising other land cover changes, it also visualises the other changes. The viewer enables us to load our own Cloud-Optimized GeoTIFFs (COGs), has the capability to fade between years, and to overlay vector boundaries. Nothing is uploaded to a server; the imagery is read directly in the browser itself.

> [!NOTE]
> New here? Read **Interface Overview**.

## Contents

- [Interface Overview](#interface-overview)
- [Loading Raster Imagery (COGs)](#loading-raster-imagery-cogs)
- [RGB and NDVI Modes](#rgb-and-ndvi-modes)
- [The Year Timeline](#the-year-timeline)
- [Basemaps](#basemaps)
- [Image Display Adjustments](#image-display-adjustments)
- [NDVI Legend](#ndvi-legend)
- [Vector Layers](#vector-layers)
- [Measuring](#measuring)
- [Labels](#labels)
- [Tips & Troubleshooting](#tips--troubleshooting)

---

## Interface Overview

The viewer has basically three main components:

- **The Map Canvas** — the main part where all the imagery and vector layers are displayed. All the changes and locations of layers are visualised here, corresponding to the following components.
- **Layers panel** — it is the control panel for loading imagery and vectors, choosing the basemap, and adjusting display. In short, it is split into an **Imagery · COG** section and a **Vectors** section.
- **Year timeline** — this controls the historical imagery, basically giving the ability to fade between years. It is found along the bottom and appears once we have loaded two or more dated COGs for moving between years.

<img width="1919" height="946" alt="Screenshot 2026-06-17 095127" src="https://github.com/user-attachments/assets/6005b2ca-ae01-44a9-9623-e3fd169313c5" />

You can also **drag and drop** image or vector files straight onto the map to add them.

---

## Loading Raster Imagery (COGs)

The viewer has the capability of loading and displaying COG (Cloud-Optimized GeoTIFF) files that we add ourselves. However, by default, the mosaics of 2015, 2016, 2017, 2018, 2019, and 2020 are added in the layer panel, which is done by streaming their COG files from GitHub.
> [!NOTE]
> The default mosaics were derived from Sentinel 2 and Landsat 8 Imagery, however the mosaics were generated only during the **Dry Periods** of Meghalaya.

Therefore, the steps are as follows:

1. In the **Imagery · COG** section, click **Load COG files** to add your COG data.
2. For the timeline feature, select **two or more** of your 8-bit COGs to build a timeline.
3. The **year for each image is read from its filename**, so name your files consistently (e.g. include `2015`, `2016`, … in the name).

In the COG imagery panel, the eye icon represents the ability to turn off or turn on the layer's visibility on the Map Canvas. Additionally, use **Clear imagery** to remove all loaded COGs and start over.

<img width="284" height="386" alt="image" src="https://github.com/user-attachments/assets/f1827aa4-0ff1-443e-82eb-f145ec833962" />

> [!TIP]
> A single COG will display, but you need at least two dated COGs for the year timeline and the fade-between-years comparison to work.

<img width="1919" height="944" alt="image" src="https://github.com/user-attachments/assets/5398565b-005b-4a44-a720-9d9c913e1a85" />


---

## RGB and NDVI Modes

The imagery can be viewed in two modes:

- **RGB** — To shows the imagery in as a colour composite.
- **NDVI** — shows the vegetation index instead, the colour-ramped ranges from water and bare ground through to dense forest. This is the quickest way to read vegetation health and spot loss as well as for comparing with the colour composite layer, mainly for verification.

Switch between them at any time and also the year timeline applies to whichever mode is active.

---

## The Year Timeline

This is the core tool for checking deforestation or any other land-use / land-cover changes. As mentioned, once two or more dated COGs are loaded, a timeline appears along the bottom of the screen.

- **Drag to fade between years** — For manually sliding along the timeline to fade from one year's image to the next, so changes in forest cover and the other land changes as we move on.
- **Snap to year** — To jump directly to a specific year, so the transition does not give a blended/fading visual effect and directly goes year to year. On the contrary, if it is turned off, the transition shows a mixed and blended land change between the two years.
- **Play / speed** — To animate through the years automatically and for adjusting the playback speed for proper change observation.

<img width="630" height="159" alt="image" src="https://github.com/user-attachments/assets/7a89d929-f470-487e-b991-751026b2b94a" />

This enables us to fade between an earlier and a later year, for example, doing this over the same patch of forest is the fastest way to see where cover has been lost.

---

## Basemaps

Within the imagery section, the following display settings are found: the basemap, an auto colour fix, band combinations, and brightness adjustment. The highlighted settings icon is where we can access the display settings.

<img width="271" height="861" alt="Screenshot 2026-06-17 100325" src="https://github.com/user-attachments/assets/af1bba31-4c32-4e5e-bbce-272c63a542a0" />

As seen in the image below, we can choose the background shown beneath the imagery and vectors. Basemaps are purely for visual assistance, and they are as follows:

- **Satellite (Esri)** — provided by Esri, it helps you work out what's on the ground through satellite.
- **Streets (OSM)** — a drawn map of the world by OpenStreetMap. It is free and made by volunteers. Unlike Esri, it is not photos; it shows roads, rivers, the names of towns and villages, and boundaries.
- **Dark canvas** — a plain, dark, low-brightness background. Best for highligting your imagery, the NDVI colours, and bright vector layers stand out, since nothing in the background competes with them.
- **None** — basically no background at all (blank). Best used when we want only our own layers visible.

<img width="288" height="441" alt="image" src="https://github.com/user-attachments/assets/69eff1e5-8fb4-4eb8-84bf-446e53c6831d" />

---

## Image Display Adjustments

These are the sets of controls for tuning and refining the COG files. However, this would usually only be needed if an image looks wrong (off-colour or too dark/bright).

**JPEG / WebP colour fix** — this handles COGs whose colour needs converting from YCbCr to RGB. In the viewer it does it automatically, hence:

- **Auto-detect (recommended)** — it detects and fixes YCbCr JPEG/WebP COGs automatically. (You can also force this on or off manually.)

However, DEFLATE- or LZW-compressed COGs do not need this fix.

**Band combo** — it is for multi-band mosaics and is for choosing which bands map to red/green/blue. However, for now only **Natural · B4 B3 B2** is available.

**Brightness (8-bit stretch · Max per band, Min 0)** — this is for adjusting and setting the maximum value for the R, G, and B bands. This is like QGIS's **Stretch to MinMax**: copy the R/G/B *Max* values from QGIS into the matching fields here. For example, a **lower max makes the image brighter**.

---

## NDVI Legend

When we click on the NDVI section, we can add our NDVI to visualise the calculated NDVI. It is a very useful index, especially when applied side by side with a true-colour composite. To make the shades understandable in the viewer, the colour ramp basically highlights the shades from water to dense vegetation.

Basically —

**water → bare → sparse → dense**

Low values correspond to water and bare ground; high values to sparse and then dense vegetation, visualised as green shades. Best used to read vegetation health at a glance and for further verification to confirm areas flagged as loss.

---

## Vector Layers

We can add vector layers and overlay boundaries and other vector data on top of the imagery.

<img width="290" height="309" alt="Screenshot 2026-06-17 095942" src="https://github.com/user-attachments/assets/8b5e5d31-4fbd-4dda-9bab-145667c2952f" />

1. In the **Vectors** section, click **Add vector** (or drag the files onto the map).
2. Supported formats:
   - **KML**
   - **GeoJSON**
   - **Shapefile** — select the `.shp`, `.dbf`, and `.prj` parts together, or load a single `.zip`.
   - **GeoPackage** (`.gpkg`)

Use **Clear vectors** to remove all vector layers.

> [!IMPORTANT]
> For shapefiles, the `.shp` on its own is not enough — include at least the `.dbf` and `.prj` (or zip the whole set), or the layer won't load correctly.

---

## Measuring

The viewer also includes the ability to measure distance and area, with two buttons located at the top-right of the map. Click a button to turn that mode on (it highlights orange), then click on the map to measure distance or area. The active mode shows a prompt telling you what to do. In both modes you click to drop points and double-click on the last point to complete the measurement.

<img width="295" height="114" alt="Screenshot 2026-06-17 123145" src="https://github.com/user-attachments/assets/36f38588-3e55-40e5-a71b-077419021dd5" />

<img width="315" height="119" alt="Screenshot 2026-06-17 123046" src="https://github.com/user-attachments/assets/b9fff22e-ecc9-448a-91df-543b8accd2a3" />

**Distance** (the ruler / diagonal-line icon) — to measure distance, create a starting point and move along a path; the distance will be in metres up to 1000 m, and then in kilometres beyond that. We can create multiple segments to find the distance of a route, and then double-click to finish, therefore giving us the total length.

<img width="1191" height="760" alt="image" src="https://github.com/user-attachments/assets/e94f6a97-0a6c-4e61-b707-42e13ac45d99" />

**Area** (the polygon icon) — for measuring the area, we have to click 3 or more points to outline a polygon shape, then double-click to finish. This will give the enclosed area, with its area calculated in hectares; alongside it, the perimeter is also generated in kilometers. We can also download the drawn polygon as a KML file and upload it into Google Earth or QGIS, etc.

<img width="1918" height="958" alt="image" src="https://github.com/user-attachments/assets/8d9e12e2-d7d1-4330-88f0-60acf2462791" />

For example, the downloaded KML opened in Google Earth perfectly reflects the polygon's location and shape.

<img width="1919" height="1032" alt="image" src="https://github.com/user-attachments/assets/d7049b96-da74-4579-a59d-2da78c6f6035" />

---

## Labels

Within the Vector layer panel, we can either hide or show text labels such as a name or ID of the added vector layer. Therefore, to turn a layer's labels on or off, click on the **tag / bookmark icon** on that layer's row in the Vectors panel.

To assist in finding the vector layer on the map, we can also **zoom to** the layer by clicking on the box-like icon next to the visibility icon. Lastly, we can also remove a layer by either clicking **Clear vectors** to remove all the layers, or clicking on the **✕** (close) icon to remove it individually.

<img width="274" height="127" alt="image" src="https://github.com/user-attachments/assets/354920b4-b276-4938-91cf-4fe3d4aaf704" />

---

## Tips & Troubleshooting

- **No timeline appears:** you need at least two COGs, and each must have a recognisable year in its filename.
- **Image too dark or washed out:** adjust the R/G/B *Max* values under Brightness — lower values brighten the image.
- **Shapefile won't load:** make sure you selected all its parts together (`.shp` + `.dbf` + `.prj`) or loaded it as a `.zip`.
- **Comparing the same spot across years:** use the year timeline's fade rather than reloading images.
