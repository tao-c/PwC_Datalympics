'''
Feature filtering object for reducing the dimensionality of the feature vectors
'''
import pandas as pd
from util.Distribution import Distribution
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, chi2
from sklearn import preprocessing

class FeatureFilter:
    def __init__(self):
        self.__dataFrame = None # data frame with features and values
        self.__meaingfulFeatures = set() # features to be used after filtering. (str)
        self.__reducedDimension = 0 # number of meaningful feature vectors

    def PCA(self, raw_attributes, numOfComponents):
        '''
        Principal component analysis.
        Filter algorithm to retrieve meaningful feature attributes.
        
        :param: 
            raw_attributes: unfiltered data
            numOfComponents: number of components to be used.
        
        :return: filtered feature vector (data frame)
        '''
        pca = PCA(n_components = numOfComponents)
        keyFeaturesVector = pca.fit_transform(raw_attributes)
        return keyFeaturesVector

    def get_reduced_dimension(self):
        '''
        Return the reduced dimension of reduced feature vectors

        :param: None
        :return: dimensionality of feature vector (int)
        '''
        return self.__reducedDimension
