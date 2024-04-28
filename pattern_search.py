def pattern_search(P, I):
   def turn(L):	
      def turn_reversed(L):
         def sum_columns(L):
            if len(L)==1: return L[0]
            return L[0]+sum_columns(L[1:])
         def new_element(L):   
            result=[]
            for ı in range(0,len(L)): 
               result.append(L[ı][0])
            return sum_columns(result)
         def remove_first(L):
            for ı in range(0,len(L)): L[ı]=L[ı][1:]
            return L  
         S=L[:] 
         result=[new_element(L)]
         ı=0
         while ı<len(S[0])-1:
            result.append(new_element(remove_first(L)))
            ı += 1  
         return result 
      def reverse_mylist(L):
         result=[]
         for x in range(0,len(L)): result.append(L[x][::-1])
         return result
      return reverse_mylist(turn_reversed(L))
   P0=P
   B=P[:]
   P1=turn(B)
   B1=P1[:]
   P2=turn(B1)
   B2=P2[:]
   P3=turn(B2)
  
   def search(N,L):
      R=[]
      ı=0
      while ı<=len(L)-len(N):
         if L[ı].find(N[0])==-1: ı += 1
         else: 
            R.append((ı,L[ı].find(N[0])))
            ı += 1
      return R
   def check_1(t,L): 
      R=False
      for ı in range(len(L)):
         if I[t[0]+ı].find(L[ı]) == t[1]: R=True
         else:
            R=False
            break
      return R    
   def check(L,İ):
      result=False
      for ı in range(len(search(L,İ))):
         if check_1(search(L,İ)[ı],L)==True: 
            result=search(L,İ)[ı]
            break
         else: continue   
      return result
   def reducer(L):
      for ı in range(len(L)): L[ı]=L[ı][1:]
      return L
   def deepcheck(L1,L2,L3,L4,İ,j):
      if check(L1,İ) != False: return [check(L1,İ),j,0]       
      if check(L2,İ) != False: return [check(L2,İ),j,90]
      if check(L3,İ) != False: return [check(L3,İ),j,180]
      if check(L4,İ) != False: return [check(L4,İ),j,270]
      if len(İ[0])<len(P[0]): return False
      else: return deepcheck(L1,L2,L3,L4,reducer(İ),j+1)
   A=deepcheck(P0,P1,P2,P3,I,0)
   if A==False: return False
   else:   
      a=A[0][0]
      b=A[0][1]+A[1]
      c=A[2]
      return (a,b,c)      
