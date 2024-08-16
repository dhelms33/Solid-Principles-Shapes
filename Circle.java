public class Circle extends Shape {
    private double radius;

    private double getArea(radius) {
        return (" Area of a circle: " + Math.PI * radius * radius);
    }

    @Override
    private double getPerimeter(radius) {
        return("Perimeter of a circle: " + 2 * Math.PI * radius);
    }

    @Override
    private void printShape() {
        System.out.println("This is a circle: ");
        System.out.println(". -- ~~~ -- .");
        System.out.println(".-~               ~-.");
        System.out.println("/                     \"");
        System.out.println("|                       |");
        System.out.println(""\                     /"");
        System.out.println("  ~-._             _.-~");
        System.out.println("      ~--.     .--~");


        
    }

}