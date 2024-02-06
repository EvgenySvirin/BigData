Вот не работает с таким логом:

Traceback (most recent call last):
  File "/usr/local/lib/python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/local/lib/python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/tmp/pyflink/1477a97e-c27d-44fd-8fe0-005adfa6a19a/15155836-601e-433d-b4d4-1bec4b62b1df/device_job1.py", line 62, in <module>
    python_data_stream_example()
  File "/tmp/pyflink/1477a97e-c27d-44fd-8fe0-005adfa6a19a/15155836-601e-433d-b4d4-1bec4b62b1df/device_job1.py", line 51, in python_data_stream_example
    env.execute_async("Devices preprocessing")
  File "/opt/flink/opt/python/pyflink.zip/pyflink/datastream/stream_execution_environment.py", line 778, in execute_async
  File "/opt/flink/opt/python/py4j-0.10.9.3-src.zip/py4j/java_gateway.py", line 1322, in __call__
  File "/opt/flink/opt/python/pyflink.zip/pyflink/util/exceptions.py", line 146, in deco
  File "/opt/flink/opt/python/py4j-0.10.9.3-src.zip/py4j/protocol.py", line 328, in get_return_value
py4j.protocol.Py4JJavaError: An error occurred while calling o10.executeAsync.
: org.apache.flink.util.FlinkException: Failed to execute job 'Devices preprocessing'.
        at org.apache.flink.streaming.api.environment.StreamExecutionEnvironment.executeAsync(StreamExecutionEnvironment.java:2203)
        at org.apache.flink.client.program.StreamContextEnvironment.executeAsync(StreamContextEnvironment.java:206)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.apache.flink.api.python.shaded.py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
        at org.apache.flink.api.python.shaded.py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:357)
        at org.apache.flink.api.python.shaded.py4j.Gateway.invoke(Gateway.java:282)
        at org.apache.flink.api.python.shaded.py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
        at org.apache.flink.api.python.shaded.py4j.commands.CallCommand.execute(CallCommand.java:79)
        at org.apache.flink.api.python.shaded.py4j.GatewayConnection.run(GatewayConnection.java:238)
        at java.lang.Thread.run(Thread.java:750)
Caused by: java.lang.RuntimeException: org.apache.flink.runtime.client.JobInitializationException: Could not start the JobMaster.
        at org.apache.flink.util.ExceptionUtils.rethrow(ExceptionUtils.java:321)
        at org.apache.flink.util.function.FunctionUtils.lambda$uncheckedFunction$2(FunctionUtils.java:75)
        at java.util.concurrent.CompletableFuture.uniApply(CompletableFuture.java:616)
        at java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:591)
        at java.util.concurrent.CompletableFuture$Completion.exec(CompletableFuture.java:457)
        at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:289)
        at java.util.concurrent.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1056)
        at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1692)
        at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:175)
Caused by: org.apache.flink.runtime.client.JobInitializationException: Could not start the JobMaster.
        at org.apache.flink.runtime.jobmaster.DefaultJobMasterServiceProcess.lambda$new$0(DefaultJobMasterServiceProcess.java:97)
        at java.util.concurrent.CompletableFuture.uniWhenComplete(CompletableFuture.java:774)
        at java.util.concurrent.CompletableFuture$UniWhenComplete.tryFire(CompletableFuture.java:750)
        at java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:488)
        at java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1609)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
        at java.lang.Thread.run(Thread.java:750)
Caused by: java.util.concurrent.CompletionException: org.apache.flink.util.FlinkRuntimeException: Failed to create checkpoint storage at checkpoint coordinator side.
        at java.util.concurrent.CompletableFuture.encodeThrowable(CompletableFuture.java:273)
        at java.util.concurrent.CompletableFuture.completeThrowable(CompletableFuture.java:280)
        at java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1606)
        ... 3 more
Caused by: org.apache.flink.util.FlinkRuntimeException: Failed to create checkpoint storage at checkpoint coordinator side.
        at org.apache.flink.runtime.checkpoint.CheckpointCoordinator.<init>(CheckpointCoordinator.java:337)
        at org.apache.flink.runtime.checkpoint.CheckpointCoordinator.<init>(CheckpointCoordinator.java:245)
        at org.apache.flink.runtime.executiongraph.DefaultExecutionGraph.enableCheckpointing(DefaultExecutionGraph.java:511)
        at org.apache.flink.runtime.executiongraph.DefaultExecutionGraphBuilder.buildGraph(DefaultExecutionGraphBuilder.java:317)
        at org.apache.flink.runtime.scheduler.DefaultExecutionGraphFactory.createAndRestoreExecutionGraph(DefaultExecutionGraphFactory.java:156)
        at org.apache.flink.runtime.scheduler.SchedulerBase.createAndRestoreExecutionGraph(SchedulerBase.java:361)
        at org.apache.flink.runtime.scheduler.SchedulerBase.<init>(SchedulerBase.java:206)
        at org.apache.flink.runtime.scheduler.DefaultScheduler.<init>(DefaultScheduler.java:134)
        at org.apache.flink.runtime.scheduler.DefaultSchedulerFactory.createInstance(DefaultSchedulerFactory.java:152)
        at org.apache.flink.runtime.jobmaster.DefaultSlotPoolServiceSchedulerFactory.createScheduler(DefaultSlotPoolServiceSchedulerFactory.java:119)
        at org.apache.flink.runtime.jobmaster.JobMaster.createScheduler(JobMaster.java:369)
        at org.apache.flink.runtime.jobmaster.JobMaster.<init>(JobMaster.java:346)
        at org.apache.flink.runtime.jobmaster.factories.DefaultJobMasterServiceFactory.internalCreateJobMasterService(DefaultJobMasterServiceFactory.java:123)
        at org.apache.flink.runtime.jobmaster.factories.DefaultJobMasterServiceFactory.lambda$createJobMasterService$0(DefaultJobMasterServiceFactory.java:95)
        at org.apache.flink.util.function.FunctionUtils.lambda$uncheckedSupplier$4(FunctionUtils.java:112)
        at java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1604)
        ... 3 more
Caused by: java.io.IOException: Failed to create directory for shared state: file:/opt/pyflink/tmp/checkpoints/logs/1e61bf30177ca59457ba22667b0d32a7/shared
        at org.apache.flink.runtime.state.filesystem.FsCheckpointStorageAccess.initializeBaseLocationsForCheckpoint(FsCheckpointStorageAccess.java:117)
        at org.apache.flink.runtime.checkpoint.CheckpointCoordinator.<init>(CheckpointCoordinator.java:333)
        ... 18 more

org.apache.flink.client.program.ProgramAbortException: java.lang.RuntimeException: Python process exits with code: 1
        at org.apache.flink.client.python.PythonDriver.main(PythonDriver.java:140)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.apache.flink.client.program.PackagedProgram.callMainMethod(PackagedProgram.java:355)
        at org.apache.flink.client.program.PackagedProgram.invokeInteractiveModeForExecution(PackagedProgram.java:222)
        at org.apache.flink.client.ClientUtils.executeProgram(ClientUtils.java:98)
        at org.apache.flink.client.cli.CliFrontend.executeProgram(CliFrontend.java:846)
        at org.apache.flink.client.cli.CliFrontend.run(CliFrontend.java:240)
        at org.apache.flink.client.cli.CliFrontend.parseAndRun(CliFrontend.java:1090)
        at org.apache.flink.client.cli.CliFrontend.lambda$main$10(CliFrontend.java:1168)
        at java.security.AccessController.doPrivileged(Native Method)
        at javax.security.auth.Subject.doAs(Subject.java:422)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1836)
        at org.apache.flink.runtime.security.contexts.HadoopSecurityContext.runSecured(HadoopSecurityContext.java:41)
        at org.apache.flink.client.cli.CliFrontend.main(CliFrontend.java:1168)
Caused by: java.lang.RuntimeException: Python process exits with code: 1
        at org.apache.flink.client.python.PythonDriver.main(PythonDriver.java:130)
        ... 16 more




# Что нашел

по трейсу ошибок только это https://stackoverflow.com/questions/61152416/could-not-find-a-file-system-implementation-for-scheme-nfs-in-apache-flink
ну у него проблема с хадупом как раз
Ещё видел что мб проблема с маунтом, но по семинару маунт такой:
    volumes:
    - .:/opt/pyflink
То есть все равно не знаю в чем проблема.