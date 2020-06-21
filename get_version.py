#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Version:
    def get_max(self, v1, v2):
        if int(v1) > int(v2):
            return 1
        elif int(v1) < int(v2):
            return -1

        
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1 = len(v1)
        l2 = len(v2)
        if l1 > l2:
            for i in range(l1-l2):
                v2.append('0')
        else:
            for i in range(l2-l1):
                v1.append('0')
        
        for i in range(len(v1)):
            r = self.get_max(v1[i], v2[i])
            if r in (1, -1):
                return r
        return 0