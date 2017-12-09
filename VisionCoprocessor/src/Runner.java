import org.opencv.core.Core;

public class Runner {

    public static void main(String[] args){
        //System.out.println(Core.NATIVE_LIBRARY_NAME);

        //System.load(new File("/usr/local/Cellar/opencv/2.4.10.1/share/OpenCV/java/libopencv_java2410.dylib").getAbsolutePath());'


        LightFinder vprocess = new LightFinder();
        while(true) {
            long millis = System.currentTimeMillis();
            //code to run
            try {
                Thread.sleep(1000 - millis % 1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            //vprocess.process();
        }//While

    }

}
