# Soil Cluster Mapping with UAVs
 
## 1) Data-stack
RGB Camera<sup>1</sup>:
 - Red
 - Green
 - Blue

NIR Camera<sup>2</sup>:
- Red
- Green
- Nir

multispectral Camera <sup>3</sup>:
- Red
- Green
- Rededge
- Nir

For reasons of spatial resolution and that the cameras did not all capture exactly the same area, two stacks were created (see Code [GetChannel.ipynb](https://github.com/carobro/VP2_SoilMapping/blob/main/Code/DataStack.ipynb)). These were brought to the same spatial resolution

 1) Red<sup>1</sup>, Green<sup>1</sup>, Blue<sup>1</sup>, NIR<sup>2</sup>, NDVI (calculated)<sup>2</sup>, Rededge <sup>3</sup>
 2) Red<sup>1</sup>, Green<sup>1</sup>, Blue<sup>1</sup>, NIR<sup>3</sup>, NDVI (calculated)<sup>3</sup>, Rededge <sup>3</sup>

## 2) Training data
2.1   Test and training data were recorded in QGIS (as points and polygons), which is important for model training and validation. (see Code [Create_TestTrainData.ipynb](https://github.com/carobro/VP2_SoilMapping/blob/main/Code/Create_TestTrainData.ipynb))

2.2 The stacks have been cut to smaller areas where the clay is definitely visible on bare fields.

## 3) Pre-Processing and Filtering
ToDo
==> increase Saturation/contrast; decrease lightning
==> Erosion Filter


## 4) Object based image classification
Create an OBIA based on the stack and the collected training data (see Code [OBIA.ipynb](https://github.com/carobro/VP2_SoilMapping/blob/main/Code/OBIA.ipynb))
![image](https://user-images.githubusercontent.com/38653703/141288661-c36f6be5-c614-43c5-a76a-a30acef0851c.png)


## 5) Validation
Validate the model with the collected test data using a confusion matrix and calculated indices. (see Code [Validation.ipynb](https://github.com/carobro/VP2_SoilMapping/blob/main/Code/Validation.ipynb))

![image](https://user-images.githubusercontent.com/38653703/141287180-56ee9721-7778-442b-9726-3bf34b778abe.png)

## 6) Model Transfer
Apply the model to other areas and check with the eye whether the classification is successful. (see Code [Model_Transfer.ipynb](https://github.com/carobro/VP2_SoilMapping/blob/main/Code/Model_Transfer.ipynb))

![image](https://user-images.githubusercontent.com/38653703/141287268-67bee1fd-e507-4fda-9dfe-b5c35145ff9c.png)
![image](https://user-images.githubusercontent.com/38653703/141288150-9284110d-60d5-4a6f-b742-ed06b2dd7db4.png)

## 7) Provide Results
ToDo
==> Raster to Polygon
==>
