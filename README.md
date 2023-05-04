# Simulation-Distributed-System
模拟Distributed System(分布式系统)的计算机通信过程

思路分析：

  模拟一个分布式系统，该系统由多台设备组成，彼此之间能够互通消息
  
  每一个设备(Device)都有一个非负整数作为ID
  
  当一个Device发现它有一个可能会影响到其他设备的问题的时候，会发出警告，采用Propagate(传播)的过程，即将信息发到多个设备组成的subset(子集)里，然后再分发到各个其他设备(P-to-P协议)
  
  每一个Alert都有个description，一个很短的string，用来唯一标识
  
  当Alert解除时，一个device会发出cancellation，通知其他devices这个Alert失效了，当一个device得知Alert失效，它将不会传递Alert给其他device
  
  Propagation Set:每一个device都能将Alert或者cancellation的信息发到一个预先设计好的collections里，形成一个Propagation Set
  
  当device新收到一条Alert或者cancellation消息的时候，会将它发到Propagation Set里，即使set里有一些device已经 知道了，收发消息会产生delay
